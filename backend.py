from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import classify_local

app = Flask(__name__)

'''
TODO
-Improve ML component by doing it for reals (AutoML Vision for spectrograms)
    -To do so I must first be able to convert from audio to spectrogram
    -THEN I can flex the accuracy

-Upload the images to a MongoDB database?
-Redo logo
-Rename to Trackea or Tracheo
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

            diagnosis = classify_local.classify(filename)
            
            return render_template("upload.html", diagnosis=diagnosis, img_filename=filename)
            # return jsonify(diagnosis_dict)
            # image = request.files["image"]
            # print(image, type(image))
            # image.save(os.path.join(app.config["IMAGE_UPLOADS"]), image.filename)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)