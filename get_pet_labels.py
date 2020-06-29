#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Vishal Ashok Hegde
# DATE CREATED: 20.05.2020
# REVISED DATE: 21.05.2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from fileinput import filename
from os import listdir


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from the folder pet_images/
    filename_list = listdir(image_dir)

    # Creating an empty dictionary with filenames and corresponding labels
    results_dic = dict()
    # Creating an empty list for pet labels
    pet_label = []

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for i in range(0, len(filename_list), 1):

        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if filename_list[0] != ".":
            # Splits string by'_' to break into words
            image_name = filename_list[i].split("_")
            # Create pet_label as empty string
            pet_name = ""

        # Loops to check if word in pet_label is only alphabetic char.
        # If true, append word to pet_label separated by trailing space
        for word in image_name:
            if word.isalpha():
                pet_name += word.lower() + " "

        # Strips of starting/trailing whitespace characters
        pet_name = pet_name.strip()
        pet_label.append(pet_name)

        if filename_list[i] not in results_dic:
            results_dic[filename_list[i]] = [pet_label[i]]
        else:
            print("**Warning:key=", filename_list[i], " already exists in results_dic with value=",
                  results_dic[filename_list[i]])

    print("Printing all Key-Value pairs in dictionary result_dic")
    for key in results_dic:
        print("Filename=", key, " Pet label=", results_dic[key])

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


#results_dic = get_pet_labels("/Users/vishalashokhegde/Desktop/Udacity/Pre_Trained_Identifiers_Dog_Breeds/pet_images/")
# Determines the number of items in the dictionary
#items_in_dic = len(results_dic)
#print("\nEmpty Dictionary results_dic -n items=", items_in_dic)
