from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.logger import info
import zipfile

class ShibokenRecipe(PythonRecipe):
    version = '6.3.1'
    wheel_path = '/home/shyamnath/qt_for_python/pyside-setup/dist/shiboken6-6.3.1-6.3.1-cp36-abi3-android_aarch64.whl'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def build_arch(self, arch):
        ''' Unzip the wheel and copy into site-packages of target'''
        info('Installing {} into site-packages'.format(self.name))
        with zipfile.ZipFile(self.wheel_path, 'r') as zip_ref:
            info('Unzip wheels and copy into {}'.format(self.ctx.get_python_install_dir(arch.arch)))
            zip_ref.extractall(self.ctx.get_python_install_dir(arch.arch))

recipe = ShibokenRecipe()
