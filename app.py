# import os
# from datetime import datetime
# from flask import Flask, render_template, jsonify, redirect, url_for, request, send_from_directory

# app = Flask(__name__)
# app.config.from_object(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'

# ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']


# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             now = datetime.now()
#             filename = os.path.join(app.config['UPLOAD_FOLDER'], "%s.%s" % (now.strftime("%Y-%m-%d-%H-%M-%S-%f"), file.filename.rsplit('.', 1)[1]))
#             file.save(filename)
#     	    return redirect(url_for('uploaded_file', filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form action="" method="post" enctype="multipart/form-data">
#       <p><input type="file" name="file" accept="video/*;capture=camera">
#          <input type="submit" value="Upload">
#     </form>
#     '''
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# @app.route('/show/<filename>')
# def uploaded_file(filename):
#     filename = 'http://127.0.0.1:5000/uploads/' + filename
#     return render_template('template.html', filename=filename)

# @app.route('/uploads/<filename>')
# def send_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from test import modify_image
UPLOAD_FOLDER = '/Users/anubhav/Documents/GithubRepos/selfie-flask-app/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print request
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            modify_image(file_path)
            modified_path = filename.split('.')[0] + '_modified.jpg'
            return redirect(url_for('send_file', filename=modified_path))
    return render_template('index.html')

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
