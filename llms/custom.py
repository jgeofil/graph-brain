# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
from typing import Dict, List, Union

from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

# [START aiplatform_predict_custom_trained_model_sample]from gbrain.hog import response


def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    instances: Union[Dict, List[Dict]],
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    """
    `instances` can be either single instance of type dict or a list
    of instances.
    """
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # The format of each instance should conform to the deployed model's prediction input schema.
    instances = instances if isinstance(instances, list) else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
    ]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    # The predictions are a google.protobuf.Value representation of the model's predictions.
    predictions = response.predictions
    for i, prediction in enumerate(predictions):
        # Convert protobuf Value to Python dict
        prediction_dict = dict(prediction)

        # Adjust this key based on your model's output schema
        # Common keys: 'video', 'output', 'generated_video', 'bytes'
        video_b64 = prediction_dict.get("video") or prediction_dict.get("output")

        if video_b64:
            try:
                video_bytes = base64.b64decode(video_b64)
                filename = f"output_{i}.mp4"
                with open(filename, "wb") as f:
                    f.write(video_bytes)
                print(f"Saved video to {filename}")
            except Exception as e:
                print(f"Error decoding video: {e}")
        else:
            print(" prediction:", prediction)


# [END aiplatform_predict_custom_trained_model_sample]
if __name__ == "__main__":
    response = predict_custom_trained_model_sample(
        project="333248287799",
        endpoint_id="8318024266939367424",
        location="us-central1",
        instances=[
            {
                "text": "A cat waving a sign that says hello world",
                "image": "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/wan_i2v_input.JPG",
            }
        ],
    )
    print(response)
