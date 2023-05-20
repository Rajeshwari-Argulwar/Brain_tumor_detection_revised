# Deep Learning Model for Brain Tumor Detection
This project implements a deep learning-based brain tumor detection system using Convolutional Neural Networks (CNN). The system aims to assist medical professionals in accurately identifying brain tumors in MRI images, enabling early detection and diagnosis of brain-related conditions. The CNN model has been trained on a diverse dataset of MRI images to ensure robust and reliable tumor detection.

## Features 
Accurate Tumor Detection: The CNN model has been trained to accurately detect brain tumors in MRI images, providing reliable results for medical analysis. User-Friendly GUI: The system includes a graphical user interface (GUI) implemented with Tkinter, making it easy to interact with the application and perform tumor detection tasks effortlessly. Tumor Region Visualization: In addition to tumor detection, the system offers the capability to visualize the tumor region within the MRI image. This feature assists in further analysis and examination by medical professionals. Usage

## Dataset
Dataset Preparation The dataset used for training the model consists of two classes: "yes" (tumor present) and "no" (tumor absent). The images are loaded from the respective directories and resized to a fixed input size of 64x64 pixels. The pixel values of the images are normalized to ensure consistent training.

## Model Architecture
Model Architecture The model architecture consists of multiple layers. It starts with a series of three convolutional layers, each followed by a max pooling layer for downsampling. The output is then flattened and passed through a fully connected layer with 64 units and a ReLU activation function. Dropout is applied to prevent overfitting, and finally, a dense layer with a sigmoid activation function is used for binary classification.

## Usage 
To use the trained model for brain tumor detection, load the saved model and pass the preprocessed MRI images to it for prediction. The model will output the probability of tumor presence. A threshold can be applied to classify the prediction as positive or negative based on the desired sensitivity and specificity.

## Acknowledgments 
We acknowledge the contributions from the deep learning and medical imaging communities, which have made advancements in the field of brain tumor detection possible. Their efforts in research and development have paved the way for the creation of models like this, enabling early detection and improved patient care.

