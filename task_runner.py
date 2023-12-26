import subprocess

commands = [
    "python getter.py",
    "python processor.py",
    "python uploader.py",
]

for cmd in commands:
    print(f"Running command: {cmd}")
    subprocess.run(cmd, shell=True)
    print(f"Completed command: {cmd}")
