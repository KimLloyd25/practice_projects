### This code creates a folder structure based on an Excel file input by the user. ###
### The Excel file should contain two columns: "Folder" and "Subfolders". ###
### The "Subfolders" column can contain multiple subfolder names separated by commas. ###
### The script checks if the specified folders and subfolders exist, and creates them if they do not. ###
### It also handles user input for the file path and validates it. ###

#Import necessary libraries
import pandas as pd
import os

#Prompt user for the path to the folder structure Excel file
path = input("Enter the path to the folder structure Excel file: ")

#Check if the path ends with .xlsx and if it exists
while not path.endswith('.xlsx'):
    print("Please enter a valid Excel file path ending with .xlsx")
    path = input("Enter the path to the folder structure Excel file: ")

#Check if the specified path exists
if not os.path.exists(path):
    # If the path does not exist, print an error message
    print("The specified path does not exist.")
# If the path exists, read the Excel file
else:
    folder_structure = pd.read_excel(path)
    # Display the contents of the DataFrame
    for index, row in folder_structure.iterrows():
        # Extract folder and subfolder names from the DataFrame
        folder = row["Folder"]
        subfolder = row["Subfolders"]

        # Create the main folder if it does not exist
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        # If the folder already exists, print a message
        else:
            print(f"Folder already exists: {folder}")
        
        # Split the subfolders by comma
        subfolders = row["Subfolders"].split(",")
        
        # Create each subfolder if it does not exist
        for subfolder in subfolders:
            # Strip whitespace from subfolder names
            subfolder = subfolder.strip()
            # Construct the full path for the subfolder
            subfolder_path = os.path.join(folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                # Print a message indicating the subfolder was created
                print(f"Created subfolder: {subfolder_path}")
            # If the subfolder already exists, print a message
            else:
                print(f"Subfolder already exists: {subfolder_path}")
    # Print a success message after creating all folders and subfolders
    print("Folder structure created successfully.")
