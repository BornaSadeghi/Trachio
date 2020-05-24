import requests, base64

def encode_image(img_filename):
    with open(img_filename, "rb") as img_file:
        return base64.b64encode(img_file.read())

encoded_img = encode_image("test/healthy.jpg")

url = "https://automl.googleapis.com/v1/projects/trachio/locations/us-central1/models/lung_sound_model:predict"

request = {
  "payload": {
    "image": {
      "imageBytes": encoded_img
    }
  },
  "auth": {}
#   "params": {
#     "scoreThreshold": "0.5"
#   }
}

response = requests.post(url, request)

print(response.text)

'''
gcloud projects add-iam-policy-binding trachio \
   --member="serviceAccount:lung-sound-user@trachio.iam.gserviceaccount.com" \
   --role="roles/automl.editor"

gcloud auth activate-service-account --key-file C:/Users/Borna/source/Lung-Sounds-Diagnosis/trachio-credentials.json
'''