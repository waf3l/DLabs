Setup the dev env:
- git clone
- cd project direcotry
- python3 -m venv /path/tp/venc
- pip install
- activate venv
- start the app by running command "python main.py" or "uvicorn main:app --reload"


***Warning***
Before run pip install -r requirements.txt please run:

- pip install wheel


***Upload image***
curl -X POST "http://127.0.0.1:8000/images" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "image=@some_image.jpg"

***Get / generate thumbnail of random file***

curl --location --request GET 'http://127.0.0.1:8000/images/8x8'

Where the 8x8 is the size of thumbnail we want to get


What could be improve:
 - constants or app variable could be moved to config file
 - images saved as bloob in redis with expire date

***Build and run***
cd myProject
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage