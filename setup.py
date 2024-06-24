from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
		 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         "assets",
         "backend",
         "models"]
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], "include_files": include_files}


executables = [Executable('main.pyw', 
			    target_name='Will of Steel.exe', 
			    icon='assets/img/logo.ico', 
			    copyright='Copyright (C) Will of Steel 2018', 
			    base='gui')
]

setup(name='Will of Steel',
      version = '0.1',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
