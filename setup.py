import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == "win32":
    base "Win32GUI"
    
executables = [cx_Freeze.Executable("master.py"), base=base, icon=""]

cx_Freeze.setup(
    name="Word-to-Daneo",
    options={"build_exe": {"packages":["pygame"],
                           "included files":["racecar.png"]}},
    executables = executables
    )

