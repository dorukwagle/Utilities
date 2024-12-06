import subprocess
import os

url = "https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/"
files = []
parentDir = os.getenv("HOME")


def runCmd(cmd):
    p = subprocess.run(cmd, stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    print(p.stdout.decode("utf-8"))


if __name__ == "__main__":
    with open("firmware_files.txt", "r") as f:
        files = f.read().splitlines()

    runCmd(["mkdir", "-p", f"{parentDir}/Downloads/firmwares"])

    for file in files:
        runCmd(["wget", url + file, "-c", "-P",
                f"{parentDir}/Downloads/firmwares"])

    print("Done")
