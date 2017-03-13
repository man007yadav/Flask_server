import os
from flask import Flask,redirect,url_for
from flask import request

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)



@app.route('/upload', methods = ['GET','POST'])
def upload():
   target = os.path.join(APP_ROOT, 'static/')
   print target
   
   if not os.path.isdir(target):
   	os.mkdir(target)

   if request.method == 'POST':
      f=request.files['files']
      destination = "/".join([target, f.filename])
      print destination
      f.save(destination)
      return '200'
   else:
      return 'Upload Page'

@app.route('/upload_label', methods = ['GET','POST'])
def upload():
   target = os.path.join(APP_ROOT, 'static/')
   print target
   
   if not os.path.isdir(target):
   	os.mkdir(target)

   if request.method == 'POST':
      f=request.files['files']
      destination = "/".join([target, f.filename])
      print destination
      f.save(destination)
      return '200'
   else:
      return 'Upload Page'

@app.route('/receive_label')
def receive_label():
	#return redirect(url_for('static', filename='label.txt'))
	return redirect("/static/label.txt")
	
@app.route('/receive')
def receive():
	return redirect(url_for('static', filename='image.jpg'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
