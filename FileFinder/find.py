import os
from chardet import detect
import locale

include_ext_lists = [".txt", ".smi", ".py"]

current_locale = locale.getdefaultlocale()
def search(dirname, keyword, result_lists):
    fileslist = os.listdir(dirname)
    for filename in fileslist:
        full_filepath = os.path.join(dirname, filename)
        
        if os.path.isdir(full_filepath):
            search(full_filepath, keyword, result_lists)
        else:
            ext = os.path.splitext(full_filepath)[-1]
            if ext not in include_ext_lists:
                continue
            
            with open(full_filepath, "rb") as file:
                raw_data = file.read()
                encode = detect(raw_data)['encoding']
                if encode == "UTF-8-SIG" or encode == "UTF-16":
                    file_data = raw_data.decode(encode)
                else:
                    file_data = raw_data.decode("cp949")

                if file_data.find(keyword) >= 0:
                    result_lists.append(full_filepath)

results = []
search("c:\\임시", "안녕", results)
print(results)
