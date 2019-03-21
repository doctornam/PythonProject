from chardet import detect
import os
import argparse

def get_encoding_type(filepath):
    with open(filepath, "rb") as file:
        rawdata = file.read()
        return detect(rawdata)['encoding']
    return None

def convert_utf8(filepath, read_codec, write_codec):
    splits = os.path.splitext(filepath)
    temp_file = splits[0] + "_tmp" + splits[1]

    if read_codec == "ISO-8859-1":
        with open(filepath, 'r') as source, open(temp_file, 'w', encoding=write_codec) as target:
            target.write(source.read())
    else:
        with open(filepath, 'r', encoding=read_codec) as source, open(temp_file, 'w', encoding=write_codec) as target:
            target.write(source.read())
    
    os.remove(filepath)
    os.rename(temp_file, filepath)

def search(dirname, file_lists):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            search(full_filename, file_lists)
        else:
            file_lists.append(full_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", type=str, help="대상폴더")
    parser.add_argument("-e", "--ext", type=str, help="대상확장자")
    args = parser.parse_args()

    if args.folder is None:
        print("사용법: python change.py -f [대상폴더명] -e [옵션:대상확장자]")
    else:
        if args.ext is None:
            ext = ".txt"
        else:
            ext = args.ext
            if ext[0] != ".":
                ext = ("." + ext).lower()

        target_dir = args.folder
        file_lists = []
        search(target_dir, file_lists)
        
        for filepath in file_lists:
            ext = os.path.splitext(filepath)[1]
            if str(ext).lower() == ext:
                encoding_type = get_encoding_type(filepath)
                if str(encoding_type).lower().find("utf-8") < 0:
                    convert_utf8(filepath, encoding_type, "utf-8")
                    print("convert complete {}".format(filepath))
