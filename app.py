from flask import Flask, render_template, jsonify
import datetime
import os


app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def inicio():
    return render_template("index.html", company_name="Jovian")


@app.route("/post.html")
def post():
    return render_template("posts.html", company_name="Jovian")

    # return render_template("base-article.html")

@app.route("/contactus.html")
def contactus():
    return render_template("contactus.html")

@app.route('/aws-services/<file>.html')
def aws_service(file):
    # return render_template('aws-services/' + file)
    file_name = file.split('.')[0]
    file_name = file_name.replace('-', ' ')
    # Date today in format May, 2023
    date_today = datetime.datetime.now().strftime("%B, %Y")
    return render_template('/aws-services/aws-template.html', file_name=file_name, file=file, date = date_today)

@app.route('/aws-services.html')
def aws():
    jpg_files = [f for f in os.listdir('static/img/aws') if f.endswith('.png')]
    # sort files by name
    jpg_files = sorted(jpg_files)
    # For each element, select what is between - and .png
    file_names = [f.split('.')[0] for f in  jpg_files]
    file_no_spaces = [f.replace(' ', '-') for f in file_names]
    file_names = [f.split('-')[1] for f in file_names]
    file_names_no_spaces = [f.replace(' ', '-') for f in file_names]
    
    file_info = list(zip(jpg_files, file_no_spaces, file_names, file_names_no_spaces))
    return render_template('aws-services.html', file_info=file_info)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
