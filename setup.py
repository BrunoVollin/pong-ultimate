import sys
from cx_Freeze import setup, Executable

include_files = ["assets/", "README.md", "LICENSE"]

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],
                     "include_files": include_files}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="pong-ultimate",
    version="1.1",
    description="He will rise...",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base,
                            icon="assets/images/app-icon.ico")]
)
