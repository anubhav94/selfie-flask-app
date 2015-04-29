import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from test import modify_image
#UPLOAD_FOLDER = '/Users/anubhav/Documents/GithubRepos/selfie-flask-app/uploads'
UPLOAD_FOLDER = '/var/www/html/ubergallery/gallery-images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
INDEX = 0
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['INDEX'] = INDEX

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        word = request.form['word']
	color = request.form['color']
	app.config['INDEX'] += 1
	if file and allowed_file(file.filename):
            filename = secure_filename(str(app.config['INDEX']) + file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            modify_image(file_path, word, color)
            modified_path = filename.split('.')[0] + '_modified.jpg'
	    os.remove(file_path)
            return redirect(url_for('send_file', filename=modified_path))
    return render_template('photob.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     filename = 'http://127.0.0.1:5000/uploads/' + filename
#     return render_template('template.html', filename = filename)

@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/uploads/' + filename
    return render_template('template.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
