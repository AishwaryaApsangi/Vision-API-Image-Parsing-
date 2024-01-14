# Google Vision API Image Analysis Script

# Overview
- This Python script is designed to analyze images using Google's Cloud Vision API. It processes a CSV file containing image URLs, performs various types of analyses on these images, and outputs the results to a new CSV file. The analyses include face detection, image properties, label detection, landmark detection, logo detection, safe search detection, and object localization.

# Features
- Face Detection: Identifies faces in images along with their emotions like joy, anger, surprise, etc.
- Image Properties: Extracts dominant colors and their fractions.
- Label Detection: Detects labels (tags) associated with the image content.
- Landmark Detection: Identifies landmarks in the images.
- Logo Detection: Detects company logos present in the images.
- Safe Search Detection: Assesses the image for adult, spoof, medical, violence, and racy content.
- Object Localization: Identifies and localizes multiple objects in an image.

# Requirements
- Python 3.x
- Google Cloud Vision API
- An active Google Cloud account with Vision API enabled
- Google Cloud API credentials (JSON file)

# Setup
- Google Cloud Vision API: Ensure that the Vision API is enabled in your Google Cloud Console.
- API Credentials: Place your Google Cloud API credentials JSON file in the script's directory. The default path is set to 'C:/Users/aishwarya/Downloads/visionapi.json'.
- Python Libraries: Install required Python libraries using the following command: pip install google-cloud-vision urllib3

# Usage
- Prepare CSV File: Prepare a CSV file named '2_Case-Level_Dataset_One Page.csv' containing the image URLs.
- Run the Script: Execute the script. It reads the CSV file, analyzes each image, and writes the results to 'labels.csv'.
- Output: The output CSV file contains detailed analysis of each image, including face detection results, image properties, and other detected features.

# Output Format
The output CSV file ('labels.csv') will have the following fields:

- Image ID, Face Number, Image URL, Vertices of detected faces
- Likelihoods of joy, underexposure, blur, anger, sorrow, headwear, surprise
- Detected objects and their fractions
- Dominant colors (Red, Green, Blue)
- Landmark, logo, label information
- Safe search detections (adult, medical, spoof, violence, racy content)

# Limitations
- The script is configured for a specific CSV format and might require adjustments for different file structures.
- It processes a defined range of lines (11633 to 17258) from the input CSV file.


# Contact
For any queries or suggestions, please contact [aapsangi@falcon.bentley.edu].
