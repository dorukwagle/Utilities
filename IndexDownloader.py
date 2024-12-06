import subprocess
import os
from bs4 import BeautifulSoup
import requests

url = "https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/"
parentDir = os.getenv("HOME")



if not os.path.exists("resource"):
    os.makedirs("resource")
    

def runCmd(cmd):
    # p = subprocess.run(cmd, stdin=subprocess.PIPE,
    #                    stdout=subprocess.PIPE,
    #                    stderr=subprocess.STDOUT)
    p = subprocess.run(cmd, stdout=subprocess.PIPE,
                        shell=True)
    print(p.stdout.decode("utf-8"))
    
    
def fetchFiles(url):
    files = []
    response = requests.get(url, verify=False)
    if not url.endswith('/'):
        url += '/'
    
    
    soup = BeautifulSoup(response.content, "html.parser")
    preTag = soup.find("pre")
    
    for link in preTag.find_all("a"):
        href = link.get("href")
        if (href.endswith("../")):
            continue
        files.append(url + href)
    return files


if __name__ == "__main__":
    url = input("Enter URL: ")
    destination = input("Enter destination Folder:")
    
    if not destination: 
        destination = "resources"
        
    if not os.path.exists(destination):
        runCmd(["mkdir", "-p", destination])

    files = fetchFiles(url)

    for file in files:
        runCmd(f"wget {file} -c --no-check-certificate -P {destination}")

    print("Done")
