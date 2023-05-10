from flask import Flask, render_template, jsonify
import datetime


import os


app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 15,00,000",
    },
    {"id": 3, "title": "Frontend Engineer", "location": "Remote"},
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$150,000",
    },
]


@app.route("/")
@app.route("/index.html")
def inicio():
    return render_template("index.html", jobs=JOBS, company_name="Jovian")


@app.route("/post")
def post():
    return render_template("posts.html", jobs=JOBS, company_name="Jovian")

    # return render_template("base-article.html")

@app.route("/contactus")
def contactus():
    return render_template("pages/contact-us.html",)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route('/aws-services/<file>')
def aws_service(file):
    # return render_template('aws-services/' + file)
    file_name = file.split('.')[0]
    file_name = file_name.replace('-', ' ')
    # Date today in format May, 2023
    date_today = datetime.datetime.now().strftime("%B, %Y")
    return render_template('aws-services/aws-template.html', file_name=file_name, file=file, date = date_today)

@app.route('/aws-services')
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
    return render_template('gallery_template.html', file_info=file_info)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
