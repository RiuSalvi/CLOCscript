import os, subprocess, argparse
from lib.sendMail import sendEmail

parser = argparse.ArgumentParser(description='Scan a specified GitHub source repository with CLOC and send the output of CLOC to an email address specified')

parser.add_argument('target', metavar='target', type=str, help='The target GitHub source repository to scan.')

parser.add_argument('email', metavar='email', type=str, help='The target email address to receive the scan results.')

args = parser.parse_args()

# target = "https://github.com/AlDanial/cloc.git"
target = args.target

subprocess.check_call(["git", "clone", target])

targetFolder = target.split("/")[-1].split(".")[0]

if os.name == 'nt':
    subprocess.run(["bin/cloc-1.98.exe", targetFolder, "--out=result.txt"])
elif os.name == 'posix':
    subprocess.run(["./bin/cloc", targetFolder, "--out=result.txt"])

resultFile = open("result.txt", "r")
sendEmail(args.email, resultFile.read())
resultFile.close()
os.remove("result.txt")
print("Deleted result.txt")