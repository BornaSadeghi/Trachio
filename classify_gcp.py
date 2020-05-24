
from google.cloud import automl
import os

# TODO(developer): Uncomment and set the following variables
project_id = "trachio"
display_name = "untitled_1590329793617"
model_id = "lung_sound_model"
file_path = "healthy-test.jpg"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Borna/source/Lung-Sounds-Diagnosis/trachio-credentials.json"


prediction_client = automl.PredictionServiceClient()

print("#################################################")

# Get the full path of the model.
model_full_id = prediction_client.model_path(
    project_id, "us-central1", model_id
)

# Read the file.
with open(file_path, "rb") as content_file:
    content = content_file.read()



image = automl.types.Image(image_bytes=content)
payload = automl.types.ExamplePayload(image=image)

# params is additional domain-specific parameters.
# score_threshold is used to filter the result
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
params = {}

response = prediction_client.predict(model_full_id, payload, params)
print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))