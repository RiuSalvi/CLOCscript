import os, subprocess, argparse

parser = argparse.ArgumentParser(description='Scan a specified GitHub source repository with CLOC and send the output of CLOC to an email address specified')

parser.add_argument('target', metavar='target', type=str, help='The target GitHub source repository to scan.')

args = parser.parse_args()

# target = "https://github.com/AlDanial/cloc.git"
target = args.target

subprocess.check_call(["git", "clone", target])

targetFolder = target.split("/")[-1].split(".")[0]

if os.name == 'nt':
    subprocess.run(["bin/cloc-1.98.exe", targetFolder, "--out=result.txt"])
elif os.name == 'posix':
    subprocess.run(["./bin/cloc", targetFolder, "--out=result.txt"])

