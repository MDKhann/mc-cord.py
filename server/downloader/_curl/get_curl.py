import urllib.request
import zipfile
import os

def get_curl():
    url = "https://curl.se/windows/dl-8.1.2_3/curl-8.1.2_3-win64-mingw.zip"
    make_dirs()
    print("Downloading curl")
    urllib.request.urlretrieve(url, "curl/curl.zip")
    print("Curl downloaded")

    with zipfile.ZipFile("curl/curl.zip", 'r') as zip_ref:
        zip_ref.extractall("curl/")

def make_dirs():
    try:
        os.makedirs("curl/")
    except:
        pass