from io import BytesIO

from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
    <title> File Upload </title>
    <body>
        <h1> Automatically deployed! </h1>
        <form action="/img/" method="post" enctype="multipart/form-data">
            <input type="file" name="picture" accept="image/*">
            <input type="submit"/>
        </form>
    </body>
    """


@app.route("/img/", methods=["POST"])
def img():
    picture = request.files["picture"]

    f = BytesIO()
    picture.save(f)

    f.seek(0)   # move to front of stream
    return send_file(f, mimetype=picture.mimetype)


if __name__ == "__main__":
    app.run(debug=True)
