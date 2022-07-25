import setuptools
from pythonforandroid.recipe import PythonRecipe, CppCompiledComponentsPythonRecipe
from pythonforandroid.logger import info
import zipfile
import sh

class ShibokenRecipe(PythonRecipe):
    version = '6.3.1'
    wheel_path = '/home/shyamnath/qt_for_python/pyside-setup/dist/shiboken6-6.3.1-6.3.1-cp36-abi3-android_aarch64.whl'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def build_arch(self, arch):
        ''' Unzip the wheel and copy into site-packages of target'''
        env = self.get_recipe_env(arch)
        info('Shyam Experimentation')
        sh.echo('$PATH', _env=env)
        sh.echo('$LDFLAGS', _env=env)
        sh.echo('$CFLAGS', _env=env)

        info('Installing {} into site-packages'.format(self.name))
        with zipfile.ZipFile(self.wheel_path, 'r') as zip_ref:
            info('Unzip wheels and copy into {}'.format(self.ctx.get_python_install_dir(arch.arch)))
            zip_ref.extractall(self.ctx.get_python_install_dir(arch.arch))

# class ShibokenRecipe(CppCompiledComponentsPythonRecipe):
#     version = "6.3.1"
#     url = "https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.3.1-src/pyside-setup-opensource-src-6.3.1.tar.xz"
#     depends = ['setuptools']
#     python_depends = ['build', 'six', 'dataclasses', 'furo', 'distro']
#     call_hostpython_via_targetpython = False
#     install_in_hostpython = False
#     setup_extra_args = ["--parallel=9",
#                         "--ignore-git",
#                         "--standalone",
#                         "--limited-api=yes",
#                         "--cmake-toolchain-file=/home/shyamnath/qt_for_python/pyside-setup/toolchain-aarch64.cmake",
#                         "--qt-host-path=/home/shyamnath/Qt/6.3.1/gcc_64",
#                         "--plat-name=android_aarch64",
#                         "--module-subset=Core"
#                         "--python-target-path=/home/shyamnath/Python-aarch64-linux-android/_install",
#                         "--qt-target-path=/home/shyamnath/Qt/6.3.1/android_arm64_v8a"
#                         "--no-qt-tools",
#                         "--skip-docs"]

#     def prebuild_arch(self, arch):
#         return super().prebuild_arch(arch)

recipe = ShibokenRecipe()
