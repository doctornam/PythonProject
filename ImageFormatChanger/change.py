from myclass import MyImage
import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-f", "--folder", type=str, help="[대상폴더]")
    parse.add_argument("-e", "--ext", type=str, help="[변경될 확장자]")
    parse.add_argument("-r", "--resize", action="store_true", help="[리사이징]")
    parse.add_argument("-tw", "--width", type=int, default=500, help="[리사이징 width]")
    parse.add_argument("-th", "--height", type=int, default=500, help="[리사이징 height]")
    args = parse.parse_args()

    if args.folder is None or args.ext is None:
        print("사용법: python change.py -f [대상폴더] -e [변환될확장자]")
    else:
        myimg = MyImage(resize=args.resize, thumb_width=args.width, thumb_height=args.height)
        myimg.search_change(args.folder, args.ext, "changed")
