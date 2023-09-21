import os, subprocess

target = "https://github.com/AlDanial/cloc.git"

subprocess.check_call(["git", "clone", target])

targetFolder = target.split("/")[-1].split(".")[0]

if os.name == 'nt':
    subprocess.run(["bin/cloc-1.98.exe", targetFolder, "--out=result.txt"])
elif os.name == 'posix':
    subprocess.run(["./bin/cloc", targetFolder, "--out=result.txt"])

