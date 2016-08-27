import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI"
if sys.platform == "win64":
    base = "Win64GUI"

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Gravity Connect",             # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]main.exe",    # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}


setup(  name = "Gravity Connect",
        version = "0.1",
        description = "A connect-four like game",
        options = {"bdist_msi": bdist_msi_options,},
        executables = [Executable("main.py", base=base)])