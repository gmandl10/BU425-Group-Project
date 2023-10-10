# Functions for data extraction and processing

def read_images(type):
    """
    this functions reads the training and testing images from the directory into 
    array of images and corresponding targets. 

    Parameters
    ----------
        type (str: "Train" or "Test") - the type of dataset to which the 
        images belong. This defines whether the images are loading from the
        training set or test set.

    Returns
    -------
        np.array(input_images) (NumPy Array) - an array of the input 
        images for the models. These images are brain scans. 

        np.array(target_variables) (NumPy Array) -  the target variable affliated
        with the corresponding image. This is the type of tumor in the image's brain 
        scan. 

    """
    import os, numpy as np
    from skimage.io import imread

    if type not in ['Train', 'Test']:
        print("type must be Train or Test")
        return
    
    type = type + "ing"

    training_dir = os.getcwd() + "\Data" + "\\" + type # initialize the training/testing folder
    target_variable = [] # create a list to collect the category
    input_images = [] # create a list to collect the image data

    for sub_category in os.listdir(training_dir): # filter through each sub-category of brain image

        sub_dir = training_dir + "\\" + sub_category

        for i in os.listdir(sub_dir): # filter through each image file in the sub-category

            image_file = sub_dir + "\\" + i

            target_variable.append(sub_category) # add the class to the list

            image = imread(image_file) # read the image into an array   
            input_images.append(image) # add the image to the list
    
    return np.array(input_images), np.array(target_variable)
