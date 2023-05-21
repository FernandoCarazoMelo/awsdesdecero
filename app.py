from flask import Flask, render_template, jsonify, request
import datetime
import os


app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def inicio():
    jpg_files = [f for f in os.listdir("static/img/pubs/principal")]
    # sort files by name
    jpg_files = sorted(jpg_files, reverse=True)
    # For each element, select what is between - and .png
    file = [f.split(".")[0] for f in jpg_files]
    file_names = [f.split(".")[0] for f in jpg_files]
    file_names = [f.split("_")[1] for f in file_names]
    file_names = [f.replace("-", " ") for f in file_names]

    file_info = list(zip(jpg_files, file, file_names))
    return render_template("index.html", file_info=file_info)


@app.route("/post.html")
def post():
    return render_template("posts.html")


@app.route("/contactus.html")
def contactus():
    return render_template("contactus.html")


@app.route("/aws-services/<file>.html")
def aws_service(file):
    file_jpg = file
    file_name = file.split(".")[0]
    file_name = file_name.split("-")[1:]
    file_name = " ".join(file_name)

    date_today = datetime.datetime.now().strftime("%B, %Y")
    return render_template(
        "/aws-services/aws-template.html",
        file_name=file_name,
        file=file,
        date=date_today,
        file_jpg=file_jpg,
    )


@app.route("/aws-services.html")
def aws():
    jpg_files = [f for f in os.listdir("static/img/aws") if f.endswith(".png")]
    # sort files by name
    jpg_files = sorted(jpg_files)
    # For each element, select what is between - and .png
    file_names = [f.split(".")[0] for f in jpg_files]
    file_no_spaces = [f.replace(" ", "-") for f in file_names]
    file_names = [" ".join(f.split("-")[1:]) for f in file_names]
    file_names_no_spaces = [f.replace(" ", "-") for f in file_names]

    file_info = list(
        zip(jpg_files, file_no_spaces, file_names, file_names_no_spaces)
    )
    return render_template("aws-services.html", file_info=file_info)


@app.route("/pubs/<file>.html")
def pubs(file):
    file_name = file.split(".")[0]
    file_name = file_name.split("_")[1]
    file_name = file_name.replace("-", " ")
    file_name = file_name.replace("|", "-\n")
    # Date today in format May, 2023
    date_today = datetime.datetime.now().strftime("%B, %Y")
    return render_template(
        "/pubs/template_pubs.html",
        file_name=file_name,
        file=file,
        date=date_today,
    )


# Preguntas y respuestas correctas
preguntas = [
    {"pregunta": "¿Qué significa AWS?", "respuesta_correcta": "a"},
    {
        "pregunta": "¿Cuál es el servicio de almacenamiento de objetos en AWS?",
        "respuesta_correcta": "a",
    },
    {
        "pregunta": "¿Qué servicio de AWS se utiliza para ejecutar código sin aprovisionar servidores?",
        "respuesta_correcta": "a",
    },
    {
        "pregunta": "¿Cuál de los siguientes servicios permite el envío de emails en AWS?",
        "respuesta_correcta": "a",
    },
    {
        "pregunta": "¿Cuál es el servicio de base de datos relacional en AWS?",
        "respuesta_correcta": "a",
    },
]


@app.route("/test.html")
def test():
    return render_template("test.html")


@app.route("/submit", methods=["POST"])
def submit():
    respuestas_usuario = dict(request.form)
    respuestas_usuario.pop("submit", None)

    score = 0
    for i, pregunta in enumerate(preguntas):
        if respuestas_usuario[f"q{i+1}"][0] == pregunta["respuesta_correcta"]:
            score += 1

    len_preguntas = len(preguntas)
    return render_template(
        "test.html", score=score, len_preguntas=len_preguntas
    )


if __name__ == "__main__":
    app.run(debug=True)
