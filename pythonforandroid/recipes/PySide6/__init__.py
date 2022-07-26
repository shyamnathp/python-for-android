import setuptools
from pythonforandroid.recipe import PythonRecipe, CppCompiledComponentsPythonRecipe
from pythonforandroid.logger import info
import zipfile
from pythonforandroid.toolchain import shprint


class PySideRecipe(PythonRecipe):
    version = '6.3.1'
    wheel_path = '/home/shyamnath/qt_for_python/pyside-setup/dist/PySide6-6.3.1-6.3.1-cp36-abi3-android_x86_64.whl'
    depends = ['shiboken6']
    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def build_arch(self, arch):
        ''' Unzip the wheel and copy into site-packages of target'''
        env = self.get_recipe_env(arch)

        info('Installing {} into site-packages'.format(self.name))
        with zipfile.ZipFile(self.wheel_path, 'r') as zip_ref:
            info('Unzip wheels and copy into {}'.format(self.ctx.get_python_install_dir(arch.arch)))
            zip_ref.extractall(self.ctx.get_python_install_dir(arch.arch))

recipe = PySideRecipe()
