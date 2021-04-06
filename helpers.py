from os import path, mkdir, listdir, remove
from datetime import datetime, timedelta
from PIL import Image
import time


def prep_size(size):
    """
    Transforms size to propare values and type
    
    :param size: string with the width and heigth information like 640x480
    :returns: size value as tuple, and also size as string
    """

    size_str = size
    size_split = size_str.split('x')
    size = []
    for item in size_split:
        size.append(int(item))
    size = tuple(size)

    return size, size_str

def check_thumbnail_exist(file_path):
    """
    Check if thumbnail at given size of selected image exist.
    Compare if the create hour of the file is in 1 hour from now.
    If not we delete the file, else we can use this file

    :param file_path(str): full path with included file name 
    :returns boolean: True if we cna use it, False if we will create new file
    """
    if path.exists(file_path):

        # time create of the file
        time_create = datetime.fromtimestamp(path.getctime(file_path))
        
        # calculate the difference
        difference = datetime.now() - time_create
        
        # check if we are between 1 hour
        if difference.seconds > 3600:
            remove(file_path)
            return False
        else:
            return True
    else:
        return False

def generate_thumbnail(src_file_path, dst_file_path, size):
    """
    Generate file with thumbnail

    :param src_file_path: path with file name of source image 
    :param dst_file_path: path with file name of file to create / re use 
    :param size: tuple with information about width and heigth
    :returns: None if everything is good, ValueError if graphic type is wrong, OSError 
        when problrem with creating / saving file 
    """
    if not check_thumbnail_exist(dst_file_path):
        try:
            # create thumbnail
            im = Image.open(src_file_path)
            im.thumbnail(size)
            im.save(dst_file_path)
            return None
        except ValueError as e:
            return {"status": "error", "error_type": "ValueError", "error_msg": str(e)}
        except OSError as e:
            return {"status": "error", "error_type": "OSError", "error_msg": str(e)}
    else:
        return None
