Before run pip install -f requirements.txt please run:

""" pip install wheel """

*** Upload image ***
curl -X POST "http://127.0.0.1:8000/images" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "image=@some_image.jpg"

*** Get / generate thumbnail of random file ***

curl --location --request GET 'http://127.0.0.1:8000/images/8x8'

Where the 8x8 is the size of thumbnail we want to get