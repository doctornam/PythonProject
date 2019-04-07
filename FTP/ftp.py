import ftplib
from tqdm import tqdm
import os

def download(filepath):
    savepath = filepath.split("/")[-1]

    ftp = ftplib.FTP()
    ftp.connect("localhost", 6600)
    ftp.login("ftpuser", "1234")
    with open(savepath, "wb") as file:
        def callback_func(data):
            file.write(data)
            progress.update(len(data))
        
        size = ftp.size(filepath)
        progress = tqdm(total=size, desc="Download.....")
        ftp.retrbinary("RETR " + filepath, callback_func)

    file.close()
    ftp.close()

def upload():
    upload_filename = "/aaa.mp4"
    filepath = "aaa.mp4"
    ftp = ftplib.FTP()
    ftp.connect("localhost", 6600)
    ftp.login("ftpuser", "1234")
    with open(filepath, "rb") as file:
        def callback_upload(send):
            progress.update(len(send))

        size = os.path.getsize(filepath)
        progress = tqdm(total=size, desc="Upload.....")
        ftp.storbinary("STOR " + upload_filename, file, 1024, callback_upload)
    ftp.close()