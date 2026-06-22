from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np

model = MobileNetV2(weights="imagenet")

captions = [
    "A dog playing in the park",
    "A person standing outdoors",
    "A cat sitting on a chair",
    "A car parked on the road",
    "An object detected in the image"
]

def generate_caption(img_path):

    img = image.load_img(img_path, target_size=(224,224))
    x = image.img_to_array(img)

    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    pred = model.predict(x)

    return captions[np.argmax(pred) % len(captions)]
