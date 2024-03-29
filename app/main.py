from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from os import path, mkdir, listdir
from helpers import prep_size, generate_thumbnail, check_dir_exist, delete_files
import re
import random
import uvicorn

# App config
IMAGES_PATH = "./images"
THUMBNAILS_PATH = "./thumbnails"
THUMBNAILS_REGEX = "(^[\d]{1,4})x([\d]{1,4}$)"

app = FastAPI()


check_dir_exist(IMAGES_PATH)
check_dir_exist(THUMBNAILS_PATH)

@app.get("/")
def main():
    return {"message": "Dlabs.AI test project"}

@app.post("/images")
async def images(image: UploadFile = File(...)):
    with open(path.join(IMAGES_PATH,image.filename),'wb+') as f:
        f.write(image.file.read())
        f.close()

    return {"filename": path.join(IMAGES_PATH,image.filename)}

@app.get("/clear/{what}")
async def clear(what:str, background_tasks: BackgroundTasks):
    if what == 'thumbnails':
        background_tasks.add_task(delete_files, THUMBNAILS_PATH)
        return {"status": 'task created'}
    elif what == 'images':
        background_tasks.add_task(delete_files, IMAGES_PATH)
        return {"status": 'task created'}
    else:
        return {"status": 'error', "message":"wrong type to delete"}


@app.get("/images/{size}")
async def get_thumbnail(size):
    """ 
    Depend on size return file with thumbnail.

    If file already exist, then respons will contain cached file (cache 1h)

    :param size: string with the width and heigth information like 640x480
    :returns: thumbnail image

    """
    # validate the size given by user
    size_validation = re.match(THUMBNAILS_REGEX, size)
    
    if size_validation:
        # get proper value of size
        size, size_str = prep_size(size_validation.string)

        # get list of all uploaded images
        files_list = listdir(IMAGES_PATH)

        if len(files_list) == 0:
            raise HTTPException(status_code=404, detail="No images in database")

        # select random file
        selected_file_no = random.randint(1,len(files_list))-1

        # split extension from file name
        thumb_filename, thumb_file_extension = path.splitext(
            files_list[selected_file_no])
        
        # create thumbnail file name with size information
        thumb_size_filename = thumb_filename+'_'+size_str+thumb_file_extension
        
        # prepare paths for image processing
        src_file = path.join(IMAGES_PATH,files_list[selected_file_no])
        dst_file = path.join(THUMBNAILS_PATH,thumb_size_filename)
        # process the image
        status= generate_thumbnail(src_file, dst_file, size)

        if status is not None:
            # there were an error
            return status
        else:
            return FileResponse(dst_file)
    else:
        return {"status": "error", "message": "wrong paramater"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)