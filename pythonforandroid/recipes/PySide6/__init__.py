import os
from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.logger import info
import zipfile
from pythonforandroid.toolchain import shutil
from os.path import join, isabs
import subprocess


def run_process(args, initial_env=None):
    """
    Run process until completion and return the process exit code.
    No output is captured.
    """
    command = " ".join([(" " in x and f'"{x}"' or x) for x in args])
    info(f"In directory {os.getcwd()}:\n\tRunning command:  {command}")

    if initial_env is None:
        initial_env = os.environ

    kwargs = {}
    kwargs['env'] = initial_env

    exit_code = subprocess.call(args, **kwargs)
    return exit_code


class PySideRecipe(PythonRecipe):
    version = '6.3.1'
    wheel_path = '/home/shyamnath/qt_for_python/pyside-setup/dist/PySide6-6.3.1-6.3.1-cp36-abi3-android_x86_64.whl'
    depends = ['shiboken6']
    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def build_arch(self, arch):
        ''' Unzip the wheel and copy into site-packages of target'''

        info('Installing {} into site-packages'.format(self.name))
        with zipfile.ZipFile(self.wheel_path, 'r') as zip_ref:
            info('Unzip wheels and copy into {}'.format(self.ctx.get_python_install_dir(arch.arch)))
            zip_ref.extractall(self.ctx.get_python_install_dir(arch.arch))

        patchelf_path = shutil.which('patchelf')
        if not isabs(patchelf_path):
            patchelf_path = join(os.getcwd(), patchelf_path)
            info(f"Using {self._patchelf_path} ...")

        info('Copying Qt libraries to be loaded on startup')
        for binary in ['libQt6Core_x86_64.so', 'libQt6Gui_x86_64.so', 'libQt6Widgets_x86_64.so']:
            shutil.copyfile(join(self.ctx.get_python_install_dir(arch.arch), 'PySide6', 'Qt', 'lib', binary),
                            join(self.ctx.get_libs_dir(arch.arch), binary))

            info('Run patchelf on the Qt binaries')
            executable_path = join(self.ctx.get_libs_dir(arch.arch), binary)
            cmd = [patchelf_path, '--set-rpath', '$ORIGIN', executable_path]

            if run_process(cmd) != 0:
                raise RuntimeError(f"Error patching rpath in {executable_path}")

        shutil.copyfile(join(arch.ndk_lib_dir, 'libc++_shared.so'),
                        join(self.ctx.get_libs_dir(arch.arch), 'libc++_shared.so'))

        shutil.copyfile(join(self.ctx.get_python_install_dir(arch.arch), 'PySide6', 'Qt', 'plugins', 'platforms', 'libplugins_platforms_qtforandroid_x86_64.so'),
                        join(self.ctx.get_libs_dir(arch.arch), 'libplugins_platforms_qtforandroid_x86_64.so'))


recipe = PySideRecipe()
