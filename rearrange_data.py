import os
import shutil
import glob
from sklearn.model_selection import train_test_split

# Define the path to the images
path_to_images = 'Data'

# Define the classes
classes = ['None_seizures', 'Seizures']

# Create directories for the classes
for class_name in classes:
    os.makedirs(os.path.join(path_to_images, 'train', class_name), exist_ok=True)
    os.makedirs(os.path.join(path_to_images, 'test', class_name), exist_ok=True)

# Split the data into training and testing sets
for class_name in classes:
    # Get a list of all the images for this class
    images = glob.glob(os.path.join(path_to_images, f'Mask_image_{class_name}_*.png'))
    
    # Split the images into training and testing sets
    train_images, test_images = train_test_split(images, test_size=0.5, random_state=42)
    for image in test_images:
        shutil.move(image, os.path.join(path_to_images, 'test', class_name))
    for image in train_images:
        shutil.move(image, os.path.join(path_to_images, 'train', class_name))
        
