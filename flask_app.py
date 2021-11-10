from flask import Flask, render_template, current_app, flash, send_file
from src.forms import PostForm
from src.compressor import compress
import secrets, os, werkzeug
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['DOWNLOAD_FOLDER'] = 'static/downloads/'

rateMin = 1
rateMax = 100

def save_image(img):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(img.filename)
	image_fn = random_hex + f_ext
	image_path = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], image_fn)

	i = Image.open(img)
	i.save(image_path)

	return image_fn

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
  form = PostForm()
  rate = 1
  imgFilename = ""
  isLoading = True
  compressionDuration = 0
  return render_template(
    'upload.html', 
    form=form, 
    rate=rate, 
    imgFilename=imgFilename, 
    isLoading=isLoading,
    compressionDuration=compressionDuration
  )

@app.route('/upload',methods=['GET','POST'])
def upload():
  form = PostForm()  
  rate = form.rate.data
  imgFilename = ""
  isLoading = True
  if (form.validate_on_submit):
    if (rate < rateMin or rate > rateMax):
      flash("rate must be in range 1 to 100")
    else: 
      imgFilename = save_image(form.image.data)
      ori_image = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], imgFilename)
      compressed = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'], imgFilename)
      compressionDuration = compress(ori_image, compressed, rate)
      isLoading = False
  return render_template(
    'upload.html', 
    form=form, 
    rate=rate, 
    imgFilename=imgFilename, 
    isLoading=isLoading, 
    compressionDuration=compressionDuration
  )

@app.route('/download/<filename>') 
def return_files_tut(filename):
  file_path = app.config['DOWNLOAD_FOLDER'] + filename
  return send_file(
    file_path, 
    as_attachment=True, 
    attachment_filename=''
  )

if __name__=='__main__':
	app.run(debug=True)