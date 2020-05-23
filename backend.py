from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import classify

app = Flask(__name__)

'''
TODO
-Be able to upload an image
-Classify the image through the server

-Upload the images to a MongoDB database?
'''

app.config["IMAGE_UPLOADS"] = "uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPG", "PNG", "JPEG", "GIF"]

test = "hello"

@app.route('/')
@app.route('/upload', methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            filename = "uploads/{}".format(secure_filename(image.filename))

            image.save(filename)

            return classify.classify(filename)

            # image = request.files["image"]
            # print(image, type(image))
            # image.save(os.path.join(app.config["IMAGE_UPLOADS"]), image.filename)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)