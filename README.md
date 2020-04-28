# A Beginner's Image Recognition Challenge

## Introduction:

This is an image classification project for the class Neuro 140: Biological and Artificial Intelligence, Harvard College Spring 2020. For this project, I use different type of self-built models (CNNs and ResNets) and pre-trained models  like VGG19 and ResNet50 to classify 4 different locations at Harvard College.

Link to presentation of this project: https://docs.google.com/presentation/d/1jVYn8dZVen7DBLUj6t0NR-I47utyxPWch0GWyWvCUb4/edit?usp=sharing

## Objectives: 

I had three objectives for this project:
1. Create a model that can classify Harvard location with over 90% accuracy
2. Gain my first end-to-end experience in learning about and being able to create advanced image classification models using modern tools like Tensorflow, Jupyter Hub etc. and also using pre-trained state of the art models like VGG16 and ResNet50.
3. Make project publicly accessible with strong documentation

## Details of files:

1. neuro140_final.ipynb -> Main python notebook. Make sure you have installed all the packages mentioned in the notebook.
2. image_generate.py -> The python script to be run in the terminal to perform data augmentation
3. 'model_name'.h5 -> Saved model weights that can be loaded in the notebook, in case you don't want to spend time training models.
4. 'Data' folder -> This file has 24 * 4 train images, 6 * 4 validation images, and 3 * 4 test images. We have to use these images and our image_generate.py to generate more training data. 

## How to use the Notebook:

Follow these steps to use the notebook:
1. Clone the repository in your computer.
2. Make sure you install all the packages used in the python notebook and the python script.
3. Create 4 folders named mh, wl, sc, jh in your base directory.
4. In your anaconda terminal, to run the command 

"python image_generate.py --image data/train/X/ --output X"

5. Run the above line 4 times replacing 'X' in the command with mh, wl, sc, jh.
6. Then CUT paste the folders with generated images into data/train_gen folder. You have successfully created augmented training data.
7. Once again, create 4 folders named mh, wl, sc, jh in your base directory.
8. In your anaconda terminal, to run the command 

"python image_generate.py --image data/train/X/ --output X"

9. Run the above line 4 times replacing 'X' in the command with mh, wl, sc, jh.
10. Then CUT paste the folders with generated images into data/validation_gen folder. You have successfully created augmented validation data.
11. Your final directory structure will look like this:

Project_folder (has image_generate.py/neuro140_final.ipynb)
- data 
  - train
    - mh
    - wl
    - sc
    - jh
  - validation
    - mh
    - wl
    - sc
    - jh
  - test
    - test_images
  - train_gen
    - mh
    - wl
    - sc
    - jh
  - validation_gen
    - mh
    - wl
    - sc
    - jh

12. You are ready to run the notebook.
13. If you have any questions, reach out to: seeamnoor@college.harvard.edu
