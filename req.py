import requests

url = "http://127.0.0.1:5000/upload"
files = {'files': open('label.txt', 'rb')}
r = requests.post(url, files=files)
