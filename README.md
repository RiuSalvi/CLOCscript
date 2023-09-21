# CLOCscript
Scan a specified GitHub source repository with CLOC and send the output of CLOC to an email address specified. Supports Windows, Linux and MacOS.

## Requirements

Python 3

## Config

This project uses mailtrap to send the emails. Please configure your mailtrap credentials in a file called config.py in the root of the project. Example:
```
mailtrapUser = "055XXXXXXXXXXX"
mailtrapPass = "05cXXXXXXXXXXX"
```

## Usage 

```
python.exe .\CLOCscript.py -h
usage: CLOCscript.py [-h] target email

Scan a specified GitHub source repository with CLOC and send the output of CLOC to an email
address specified

positional arguments:
  target      The target GitHub source repository to scan.
  email       The target email address to receive the scan results.

options:
  -h, --help  show this help message and exit
```

## Example

```
python.exe .\CLOCscript.py https://github.com/AlDanial/cloc.git target@example.com
Cloning into 'cloc'...
remote: Enumerating objects: 6117, done.
remote: Counting objects: 100% (1690/1690), done.
remote: Compressing objects: 100% (647/647), done.
remote: Total 6117 (delta 1041), reused 1482 (delta 988), pack-reused 4427
Receiving objects: 100% (6117/6117), 4.20 MiB | 5.88 MiB/s, done.
Resolving deltas: 100% (3586/3586), done.
     823 text files.
     718 unique files.
     111 files ignored.
Wrote result.txt
Email with the results sent to target@example.com
Deleted result.txt
```