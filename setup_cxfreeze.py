import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
  packages = [], excludes = [],
  include_files = ['icon','toc'],
)

name = 'example'

if sys.platform == 'win32':
  name = name + '.exe'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
  Executable('main.py', base = base, targetName = name,
             compress = True,
            )
]

setup(name='Example',
      version = '1.0',
      description = 'An example program',
      options = dict(build_exe = buildOptions),
      executables = executables)