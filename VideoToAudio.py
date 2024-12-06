import subprocess
import os


def runCmd(cmd):
    p = subprocess.run(cmd, stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    print(p.stdout.decode("utf-8"))


def process_file(file):
    chunks = file.split(".")
    chunks.pop()
    destination = '.'.join(chunks) + '.m4a'
    runCmd(["ffmpeg", "-i", file, "-q:a", "0", "-map", "a", destination])

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    cwd = os.getcwd()
    files = os.listdir(cwd)

    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(process_file, files)

    executor.shutdown(wait=True)
    print("Done")
