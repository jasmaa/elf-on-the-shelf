from google_images_download import google_images_download

import os
import shutil
import time

# clear subdir
def clear(folder):
    # delete subdir contents
    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def get_files(folder):

    img_list = []
    for f in os.listdir(folder):
        print(f)
        img_list.append(folder+"/"+f)
    return img_list

# retrieve images
def get_img_from_search(search, limit=5):

    # clear images folder
    clear('images')

    # download
    resp = google_images_download.googleimagesdownload()
    resp.download({
        "keywords":search,
        "output_directory":"images",
        "limit":6,
        "size":"large",
    })

    # collect names
    return get_files("images/"+search)
