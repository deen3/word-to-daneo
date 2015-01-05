import cx_Freeze

executables = [cx_Freeze.Executable("master.py")]

cx_Freeze.setup(
    name="Word-to-Daneo",
    options={"build_exe": {"packages":["pygame"],
                           "included files":["racecar.png"]}},
    executables = executables
    )

