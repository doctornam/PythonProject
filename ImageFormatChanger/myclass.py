from PIL import Image
import os

class MyImage():
    def __init__(self, **kwargs):
        self.resize = kwargs.get("resize", False)
        self.thumb_width = kwargs.get("thumb_width", 500)
        self.thumb_height = kwargs.get("thumb_height", 500)

    def search_change(self, foldername, ext, new_folder):
        filelists = os.listdir(foldername)

        for file in filelists:
            full_path = os.path.join(foldername, file)
            if os.path.isfile(full_path):
                src_ext = os.path.splitext(full_path)[-1]
                if src_ext == ext:
                    continue
                new_filename = self.change_format(full_path, ext, new_folder)
                print("{} 변환 되었습니다.".format(full_path))

                if self.resize:
                    self.resize_image(new_filename)
                    print("{} 파일이 {} {} 리사이징 되었습니다.".format(full_path, self.thumb_width, self.thumb_height))

    def change_format(self, filename, ext, new_folder):
        target_folder = os.path.split(filename)[0] + "\\" + new_folder
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        src_filename = os.path.splitext(filename)[0]
        new_filename = target_folder + "\\" + src_filename.split("\\")[-1] + ext
        img = Image.open(filename)
        img.save(new_filename)
        return new_filename

    def resize_image(self, filename):
        img = Image.open(filename)
        width, height = img.size

        if width < height:
            aspect = height / self.thumb_height
            new_size = (int(width / aspect), self.thumb_height)
        else:
            aspect = width / self.thumb_width
            new_size = (self.thumb_width, int(height / aspect))
        img.resize(new_size).save(filename)