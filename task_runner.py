import subprocess


# not included getting files or downloading files! please get them before running this script
commands = [
    "python getter.py",
    "python processor.py",
    "python uploader.py",
]

for cmd in commands:
    subprocess.run(cmd, shell=True)