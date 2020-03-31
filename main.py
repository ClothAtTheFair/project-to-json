import pickle
import json
import argparse


def take_in_user_inputs():
    print('Welcome to Projects to List (name under review) by Bradley Faircloth.')

    projectName = input("Please input the name of the project ")
    screenshots = input("Please give the name of the screenshot you wish to be the thumbnail ")

    # There can be more than one screenshot so the type checker should be more robust
    checked_screenshots = type_checker(screenshots, "picture")

    description = input("Please give the description for the project.")
    url = input("Please give the url for the project ")

    inputs = dict(name = projectName, screenshots = checked_screenshots,
                 description = description, url = url)

    return inputs

def load_JSON(json_file):
    with open(json_file, 'r') as openfile:

        json_object = json.load(openfile)
    print(json_object)
    return json_object

def write_to_JSON(inputs, file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)

        temp = data['projects']

        temp.append(inputs)

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    

def save_JSON_to_location(path):
    pass

def type_checker(input, type):
    if type.lower() == "picture":
        fileExtension = input[-3::]
        # fileExtension should be png, svg, or jpg else it reject it
        if fileExtension.lower() == "png" or fileExtension == "svg" or fileExtension == "jpg":
            return input.lower()
        else:
            raise TypeError("screenshots are not the right file extension")

    elif type.lower() == "url":
        pass 
        #Let's get to this Wednesday

    elif type.lower() == "path":
        pass
        #to be determined    


if __name__ == "__main__":
    user_input = input("Hello, do you wish to load a json file or add to an existing one? Please say load or add to continue ")
    file_name = input("What is the file name? Please add .json on the end ")
    if user_input.lower() == "load":
        load_JSON(file_name)
    elif user_input.lower() == "add":
        first = take_in_user_inputs()
        data = write_to_JSON(first, file_name)
    else:
        print("I'm sorry, that isn't one of the options")
        exit(1)


    



