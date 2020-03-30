import pickle
import json
import argparse


def take_in_user_inputs():
    print('Welcome to Projects to List (name under review) by Bradley Faircloth.')

    newOrOld = input("Do you need a new file? Please type yes or no ")
    path = input("Please give the file path for either where you want the file or where it is currently located ")
    projectName = input("Please input the name of the project ")
    screenshots = input("Please give the name of the screenshot(s) with commas to separate multiple ones. " 
    + " The first screenshot will be considered the thumbnail ")

    # There can be more than one screenshot so the type checker should be more robust
    checked_screenshots = type_checker(screenshots, "picture")

    description = input("Please give the description for the project.")
    url = input("Please give the url for the project ")

    inputs = dict(newFile = newOrOld.lower(), filePath = path, name = projectName, screenshots = checked_screenshots,
                 description = description, url = url)

    return inputs

def check_for_JSON(file_path):
    #check to make sure the file is where the path mentions.
    #if the path is there return else throw an error
    pass

def write_to_JSON(inputs):
    pass

def save_JSON_to_location(path):
    pass

def type_checker(input, type):
    if type.lower() == "picture":
        fileExtension = input[-3::]
        # fileExtension should be png, svg, or jpg else it reject it
        if fileExtension.lower() == "png" or fileExtension == "svg" or fileExtension == "jpg":
            return fileExtension.lower()
        else:
            raise TypeError("screenshots are not the right file extension")

    elif type.lower() == "url":
        pass 
        #Let's get to this Wednesdays

    elif type.lower() == "path":
        pass
        #to be determined    


if __name__ == "__main__":
    furst = take_in_user_inputs()
    if furst["newFile"] == "no":
        check_for_JSON(furst["filePath"])
    else:
        write_to_JSON(furst)

    



