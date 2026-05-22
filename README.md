# 🌿 Plant Disease Detection using CNN and Flask

## 📌 Project Overview

Plant Disease Detection using CNN and Flask is a deep learning web application that predicts plant leaf diseases from uploaded leaf images.

This project uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset to classify plant leaves into different healthy and diseased categories. The trained model is integrated with a Flask web application where users can upload a plant leaf image and get the predicted disease name along with the confidence score.

---

## 🌐 Live Demo

🔗 **Deployment Link:**  
https://plant-disease-detection-cnn-flask.onrender.com/

---

## 🎯 Problem Statement

Plant diseases can reduce crop quality and crop yield if they are not detected early. Manual disease identification requires expert knowledge and may take time.

The goal of this project is to build a CNN-based image classification model that can identify plant leaf diseases from images and provide a simple web interface for prediction.

---

## ✅ Objective

- Build a CNN model to classify plant leaf diseases.
- Preprocess plant leaf images for deep learning.
- Train the model on multiple plant disease classes.
- Evaluate the model using test data.
- Create a Flask web application for image upload and prediction.
- Display the predicted disease name and confidence score to the user.

---

## 📊 Dataset

Dataset used: **PlantVillage Dataset**

🔗 **Dataset Link:**  
https://www.kaggle.com/datasets/mohitsingh1804/plantvillage

The dataset contains plant leaf images belonging to healthy and diseased categories.

Dataset details:

- Total images: Around 54,000+
- Number of classes: 38
- Image type: Plant leaf images
- Task type: Multi-class image classification

The dataset is organized into training and validation folders, where each class has its own folder.

Example classes:

- Apple___Apple_scab
- Apple___Black_rot
- Apple___healthy
- Corn_(maize)___Common_rust_
- Grape___Black_rot
- Potato___Early_blight
- Potato___Late_blight
- Tomato___Bacterial_spot
- Tomato___Early_blight
- Tomato___healthy

---

## 🧠 Deep Learning Approach

This project uses a Convolutional Neural Network because CNNs are highly effective for image classification tasks.

CNN helps the model learn important image patterns such as:

- Edges
- Shapes
- Leaf textures
- Disease spots
- Color variations
- Visual disease patterns

---

## 🔄 Project Workflow

1. Dataset collection
2. Image preprocessing
3. Data augmentation
4. Train, validation, and test split
5. CNN model building
6. Model compilation
7. Model training
8. Model evaluation
9. Model saving
10. Flask web app development
11. Image upload and prediction
12. Display prediction result with confidence score
13. Web app deployment

---

## 🖼️ Image Preprocessing

The uploaded image is preprocessed before sending it to the trained CNN model.

Preprocessing steps:

- Resize image to 128 x 128
- Convert image into NumPy array
- Normalize pixel values from 0-255 to 0-1
- Expand image dimensions to match model input shape

Model input shape:

    128 x 128 x 3

---

## 🧪 Data Augmentation

Data augmentation was applied to the training images to improve model generalization and reduce overfitting.

Augmentation techniques used:

- Rotation
- Zoom
- Shear transformation
- Horizontal flip
- Width shift
- Height shift
- Brightness adjustment

---

## 🏗️ CNN Model Architecture

The CNN model contains:

- Conv2D layers for feature extraction
- MaxPooling2D layers for reducing image size
- Flatten layer to convert feature maps into a 1D vector
- Dense layers for classification
- Dropout layers to reduce overfitting
- Softmax output layer for multi-class classification

Model structure:

    Input Image
        ↓
    Conv2D + ReLU
        ↓
    MaxPooling2D
        ↓
    Conv2D + ReLU
        ↓
    MaxPooling2D
        ↓
    Conv2D + ReLU
        ↓
    MaxPooling2D
        ↓
    Flatten
        ↓
    Dense + Dropout
        ↓
    Dense + Dropout
        ↓
    Dense + Dropout
        ↓
    Output Layer with Softmax

---

## ⚙️ Model Configuration

Loss function used:

    categorical_crossentropy

Optimizer used:

    Adam

Evaluation metric:

    Accuracy

Reason for using categorical_crossentropy:

The project is a multi-class classification problem with 38 classes, and the labels are one-hot encoded.

---

## 📈 Model Performance

The CNN model achieved the following test performance:

- Test Accuracy: 91.73%
- Test Loss: 0.2933

This means the model correctly classified plant leaf images with strong performance on unseen test data.

---

## 🌐 Flask Web Application

The trained CNN model is integrated into a Flask web application.

The web app allows users to:

- Open the home page
- Upload a plant leaf image
- Submit the image for prediction
- View the predicted disease name
- View the confidence score
- Upload another image for prediction

---

## 🖥️ Web App Screenshots

### Home Page

<img src="images/home-page.png" width="100%"><br>

### Upload Page Without Image

<img src="images/upload-page-without-image.png" width="100%"><br>

### Upload Page With Image

<img src="images/upload-page-with-image.png" width="100%"><br>

### Prediction Result Page

<img src="images/prediction-result.png" width="100%"><br>

---

## 📁 Project Structure

    plant_disease_detection_cnn_flask/
    │
    ├── plant_dd_cnn/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── Procfile
    │   ├── .gitignore
    │   │
    │   ├── model/
    │   │   └── plant_disease_model.keras
    │   │
    │   ├── notebook/
    │   │   └── plant_disease_detection.ipynb
    │   │
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── style.css
    │   │   │
    │   │   └── uploads/
    │   │
    │   ├── templates/
    │   │   ├── home.html
    │   │   ├── upload.html
    │   │   └── result.html
    │   │
    │   └── utils/
    │       └── preprocessing.py
    │
    └── images/
        ├── home-page.png
        ├── upload-page-without-image.png
        ├── upload-page-with-image.png
        └── prediction-result.png

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- Pillow
- HTML
- CSS
- Gunicorn
- Python-dotenv
- Render

---

## 📌 Key Features

- CNN-based plant disease classification
- Flask-based web interface
- Image upload functionality
- Automatic image preprocessing
- Disease prediction with confidence score
- Clean and responsive user interface
- Supports 38 plant disease and healthy leaf classes
- Deployed web application using Render

---

## 🚀 How the Web App Works

1. User opens the home page.
2. User clicks the upload image button.
3. User uploads a plant leaf image.
4. Flask receives the uploaded image.
5. The image is saved temporarily in the uploads folder.
6. The image is resized and normalized.
7. The trained CNN model predicts the class.
8. The predicted class index is converted into the disease name.
9. The web app displays the predicted disease and confidence score.

---

## 🔍 Prediction Flow

    Uploaded Leaf Image
            ↓
    Image Preprocessing
            ↓
    CNN Model Prediction
            ↓
    Predicted Class Index
            ↓
    Disease Name
            ↓
    Confidence Score
            ↓
    Result Page

---

## 🧾 Example Output

Example prediction result:

    Predicted Disease: Grape___Esca_(Black_Measles)
    Confidence Score: 72.8%

---

## ⚠️ Disclaimer

This project is developed for learning and educational purposes.

The prediction result should not be used as a final agricultural or scientific diagnosis. For real-world farming decisions, expert verification is recommended.

---

## 📚 Learning Outcome

Through this project, I learned:

- How CNN works for image classification
- How to preprocess image data for deep learning
- How to use ImageDataGenerator for augmentation
- How to train and evaluate a multi-class CNN model
- How to save and load a trained Keras model
- How to integrate a deep learning model with Flask
- How to build a simple end-to-end AI web application
- How to deploy a Flask deep learning application

---

## 📌 Future Improvements

- Improve accuracy using transfer learning models like MobileNetV2 or ResNet50
- Add more plant disease datasets
- Add treatment or prevention suggestions for each disease
- Improve UI with live preview before prediction
- Store prediction history using a database
- Add confidence-based warning for low-confidence predictions
- Create a mobile-friendly version of the application

---

## 👨‍💻 Author

Dhuruvan Shanker R

---

## ⭐ Project Summary

This project demonstrates an end-to-end deep learning workflow by training a CNN model for plant disease classification and deploying it through a Flask web application. The system predicts plant leaf diseases from uploaded images and displays the result with a confidence score.