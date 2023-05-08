from flask import Flask, render_template, jsonify

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


@app.route("/blog")
def blog():
    return render_template("base-article.html")

@app.route("/contact-us")
def contact():
    return render_template("pages/contact-us.html",)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
