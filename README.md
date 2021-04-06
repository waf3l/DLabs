Setup the dev env:
- git clone
- cd project direcotry
- python3 -m venv /path/to/venv
- pip install -r requirements.txt
- activate venv
- start the app by running command "python main.py" or "uvicorn main:app --reload"


***Warning***
Before run pip install -r requirements.txt please run:

- pip install wheel


***Upload image***

curl -X POST "http://127.0.0.1:8000/images" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "image=@some_image.jpg"

***Get / generate thumbnail of random file***

curl -X GET 'http://127.0.0.1:8000/images/8x8 --output thumbnail.jpg'

Where the 8x8 is the size of thumbnail we want to get

***Clear files from media storage***
Delete all uploaded and generated files, to check if app will 
return 404 when no images in database

curl -X GET 'http://127.0.0.1:8000/clear/thumbnails'
curl -X GET 'http://127.0.0.1:8000/clear/images'

***What could be improve***:

 - constants or app variable could be moved to config file
 - images saved as bloob or path information in redis (with expire date) or other database like mysql, postgresql 


***Docker build and run***

- cd myProject
- docker build -t myimage .
- docker run -d --name mycontainer -p 80:80 myimage
