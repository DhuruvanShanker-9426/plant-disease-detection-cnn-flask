import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np
from utils.preprocessing import image_preprocessing
from dotenv import load_dotenv
from PIL import Image
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)

model_path = os.environ.get("MODEL_PATH", "model/plant_disease_model.keras")
model = load_model(model_path)

upload_folder = os.environ.get("UPLOAD_FOLDER", "static/uploads")
app.config["UPLOAD_FOLDER"] = upload_folder

os.makedirs(upload_folder, exist_ok=True)

class_names = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/predict", methods=["POST"])
def predict():
    image_file = request.files.get("image")

    if image_file is None:
        return render_template(
            "upload.html",
            message="No image uploaded. Please upload an image."
        )

    image_filename = image_file.filename

    if image_filename == "":
        return render_template(
            "upload.html",
            message="No image selected. Please select an image to upload."
        )

    image_filename = secure_filename(image_filename)
    img_path = os.path.join(app.config["UPLOAD_FOLDER"], image_filename)

    image_file.save(img_path)

    input_image = Image.open(img_path)

    img_arr = image_preprocessing(input_image)

    predictions = model.predict(img_arr)

    predicted_label = np.argmax(predictions)

    predicted_class = class_names[predicted_label]

    predicted_probability = np.max(predictions) * 100
    predicted_probability = round(predicted_probability, 2)

    return render_template(
        "result.html",
        image_path=img_path,
        prediction=predicted_class,
        confidence=predicted_probability
    )


if __name__ == "__main__":
    port=int(os.environ.get("PORT", 5000))
    debug_mode=os.environ.get("DEBUG_MODE",False) == True
    app.run(host="0.0.0.0",port=port,debug=debug_mode)