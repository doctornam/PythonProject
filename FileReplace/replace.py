import argparse

def file_replace(filepath, src, tar):
    with open(filepath, "r") as file:
        content = file.read()
    content = content.replace(src, tar)
    with open(filepath, "w") as file:
        file.write(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="파일명")
    parser.add_argument("-s", "--src", type=str, help="원본문자열")
    parser.add_argument("-t", "--tar", type=str, help="치환문자열")
    args = parser.parse_args()

    if args.file is None or args.src is None or args.tar is None:
        print("사용법: python replace.py -f [파일명] -s [원본문자열] -t [치환문자열]")
    else:
        file_replace(args.file, args.src, args.tar)