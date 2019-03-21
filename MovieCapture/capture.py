import os
import subprocess
import mimetypes
import argparse
import json

def video_capture_frame(video_path, target_sec=1):
    filepath, filename = os.path.split(video_path)
    realname = os.path.splitext(filename)[0]
    image_filepath = filepath + "\\" + realname + ".jpg"
    command = 'ffmpeg -loglevel "quiet" -y -accurate_seek -ss {} -i "{}" -frames 1 "{}"'.format(target_sec, video_path, image_filepath)
    print(command)
    subprocess.call(command)

def search_dir(dirname, file_lists):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            search_dir(full_filename, file_lists)
        else:
            mimetype = mimetypes.guess_type(full_filename)[0]
            if mimetype is None:
                continue
            if mimetype.find("video") < 0:
                continue
            file_lists.append(full_filename)

def get_video_info(video_path):
    proc = subprocess.Popen(
        ["ffprobe", "-show_format", "-show_streams", "-loglevel", "quiet", "-print_format", "json", video_path], 
        stdout=subprocess.PIPE
        )
    out, err = proc.communicate()
    out_json = json.loads(out.decode('utf-8'))
    duration = out_json["format"]["duration"]
    size = out_json["format"]["size"]
    bitrate = out_json["format"]["bit_rate"]
    return {
        "duration": duration,
        "size": size,
        "bitrate": bitrate,
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--folder", type=str, help="대상폴더")
    p.add_argument("-s", "--sec", type=int, help="캡처위치(sec)")
    args = p.parse_args()

    if args.folder is None:
        print("사용법: python capture.py -f [대상폴더] -s [옵션:캡처위치(sec)]")
    else:
        sec = 3
        if args.sec is not None:
            sec = args.sec

        video_lists = []
        search_dir(args.folder, video_lists)
        for video in video_lists:
            video_info = get_video_info(video)
            if sec > int(float(video_info["duration"])):
                sec = int(float(video_info["duration"]))
            video_capture_frame(video, target_sec=sec)