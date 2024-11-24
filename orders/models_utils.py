import datetime
import os

from fastapi import UploadFile
import hashlib

PATH = "./uploads/"

def generate_random_value(filename: str) -> str:
    coder = hashlib.new("sha256")
    time = datetime.datetime.utcnow()
    coder.update((str(time) + filename).encode(encoding="utf-8"))
    return coder.hexdigest()

def save_upload_file(file: UploadFile) -> str:
    filename = file.filename
    print(filename)
    path = f"{PATH}/{generate_random_value(filename)}{filename[filename.rfind('.'):]}"
    print(path)
    try:
        with open(path, "wb+") as destination:
            destination.write(file.file.read())
    finally:
        file.file.close()

    return path

def delete_file(
        filepath: str
):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        raise FileNotFoundError("File is missing!")