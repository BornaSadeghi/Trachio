from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import classify

app = Flask(__name__)

'''
TODO
-Create option to contact local health department for potential of COVID-19


-Upload the images to a MongoDB database?
-Rename to Trackea
'''

app.config["IMAGE_UPLOADS"] = "uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPG", "PNG", "JPEG", "GIF"]

@app.route('/')
@app.route('/upload', methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            filename = "static/uploads/{}".format(secure_filename(image.filename))

            image.save(filename)

            diagnosis = classify.classify(filename)
            
            return render_template("upload.html", diagnosis=diagnosis, img_filename=filename)
            # return jsonify(diagnosis_dict)
            # image = request.files["image"]
            # print(image, type(image))
            # image.save(os.path.join(app.config["IMAGE_UPLOADS"]), image.filename)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)