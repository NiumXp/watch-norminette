import os
import re
import time
import argparse
import subprocess
import collections
from contextlib import suppress

PATTERN = re.compile(r"(\d+)\D+(\d+)\W+([\w ]+)", flags=re.A)

_path = os.getcwd()
_path = os.path.dirname(_path)

temp = collections.defaultdict(dict)

parser = argparse.ArgumentParser()
parser.add_argument("--errors", action="store_true")

args = parser.parse_args()

ERROR = args.errors


def print_repository():
    print("\n\033[1;36m[!]\033[0m https://github.com/NiumXp/watch-norminette\n")


def norminette(file):
    return subprocess.Popen(
        ["norminette", file],
        stdout=subprocess.PIPE,
    ).stdout.read().decode()


def main():
    with suppress(KeyboardInterrupt):
        while True:
            for folder, _, files in os.walk(_path):
                for file in files:
                    path = os.path.join(folder, file)

                    _, extension = os.path.splitext(file)
                    if extension == ".c":
                        if ERROR:
                            output = norminette(path)
                            firstline, *rest = output.split('\n')

                            if "r" == firstline[-2]:
                                print(f"\033[1;31m{len(rest):>3}\033[0m {path}")

                            continue

                        now = os.stat(path).st_mtime
                        old = temp[folder].setdefault(file, now)

                        if old < now:
                            os.system("clear")

                            temp[folder][file] = now

                            output = norminette(path)
                            firstline, rest = output.split('\n', 1)

                            if "OK!" in firstline:
                                print(f"{path} \033[1;32mOK!\033[0m")

                            for match in PATTERN.finditer(rest):
                                l, c, t = match.groups()
                                print(f"{path}:{l}:{c}\t\033[1;31m{t}\033[0m")

                            print_repository()

            if ERROR:
                print_repository()
                break
