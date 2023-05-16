from flask_frozen import Freezer
from app import app
import os

app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)


@freezer.register_generator
def inicio():
    yield '/index.html'
    
@freezer.register_generator
def post():
    yield '/post.html'
    
@freezer.register_generator
def contactus():
    yield "/contactus.html"
    
@freezer.register_generator
def aws():
    yield "/aws-services.html"
    
    
@freezer.register_generator
def aws_service():
    jpg_files = [f for f in os.listdir('static/img/aws') if f.endswith('.png')]
    # sort files by name
    jpg_files = sorted(jpg_files)
    # For each element, select what is between - and .png
    file_names = [f.split('.')[0] for f in  jpg_files]
    file_no_spaces = [f.replace(' ', '-') for f in file_names]

    for file in file_no_spaces:
        yield {'file': file}

@freezer.register_generator
def pubs():
    # return render_template('aws-services/' + file)
    jpg_files = [f for f in os.listdir('static/img/pubs/principal') if f.endswith('.jpg')]
    # sort files by name
    jpg_files = sorted(jpg_files, reverse=True)
    # Get file names
    file = [f.split('.')[0] for f in  jpg_files]
    file_names = [f.split('.')[0] for f in  jpg_files]
    
    for file in file_names:
        yield {'file': file}

    
if __name__ == '__main__':
    freezer.freeze()
    # freezer.run(debug=True)