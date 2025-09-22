### This is a recipes library where you can create, read and delete recipes. ###
### You can also create and delete categories within the recipe library. ###

from pathlib import Path
import os

# Choose from options:

def print_menu():
    print("\nRecipe Manager Menu:")
    print("1. Read Recipe")
    print("2. Create Recipe")
    print("3. Create Category")
    print("4. Delete Recipe")
    print("5. Delete Category")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    while choice not in ['1', '2', '3', '4', '5', '6']:
        choice = input("Invalid choice. Please enter a number between 1 and 6: ")
    if choice in ['1', '2', '3', '4', '5', '6']:
        return choice

# 1 - Read recipe
## Choose category
## List recipes
## Choose recipe
## Read recipe

def read_recipe():
    category = input("Enter the category of the recipe you want to read: ")
    category_path = Path("recipes") / category
    while os.path.isdir(category_path) == False:
        print("This category does not exist. Please choose a valid category.")
        category = input("Enter the category of the recipe you want to read: ")
        category_path = Path("recipes") / category
    if os.listdir(category_path):
        for f in os.listdir(category_path):
            print(f)
    recipe = input("Which recipe would you like to read?: ")
    while os.path.exists(category_path / recipe) == False:
        print("This recipe does not exist. Please choose a valid recipe.")
        category = input("Which recipe would you like to read?: ")
        recipe = input("Which recipe would you like to read?: ")
    if os.path.exists(category_path / recipe):
        file = open(category_path / recipe, 'r')
        print(file.read())
        input("Press any key to return to main menu")
        file.close()
    

# 2 - Create recipe
## Choose category
## Create name
## Create content

def create_recipe():
    category = input("Enter the category for the recipe you want to create: ")
    category_path = Path("recipes") / category
    while os.path.isdir(category_path) == False:
        print("This category does not exist. Please choose a valid category.")
        category = input("Enter the category for the recipe you want to create: ")
        category_path = Path("recipes") / category
    if os.listdir(category_path):
        name = input("Please enter a name for this recipe: ")
        if os.path.exists(category_path / name):
            print("This recipe already exists. Please try a different name.")
            name = input("Please enter a name for this recipe: ")
        recipe_path = category_path / (name + ".txt")
        file = open(recipe_path, 'w')
        print("Recipe file has been created.")
        content = input("Please enter the content for this recipe file: ")
        file.write(content)
        file.close()
        input("Press any key to return to main menu")
        

# 3 - Create category
## Name category
## Create category

def create_category():
    category = input("Enter the name of the category you would like to create: ")
    category_path = Path("recipes") / category
    while os.path.exists(category_path) == True:
        print("This category already exists.")
        category = input("Enter the name of the category you would like to create: ")
    if os.path.exists(category_path) == False:
        os.makedirs(category_path)
        print("The category has been created successfully")
        input("Press any key to return to main menu")

# 4 - Delete recipt
## Choose category
## List recipes
## Choose recipe
## Delete recipe

def delete_recipe():
    category = input("Enter the category for the recipe you want to create: ")
    category_path = Path("recipes") / category
    while os.path.isdir(category_path) == False:
        print("This category does not exist. Please choose a valid category.")
        category = input("Enter the category for the recipe you want to create: ")
        category_path = Path("recipes") / category
    if os.listdir(category_path):
        for f in os.listdir(category_path):
            print(f)
    recipe = input("Which recipe would you like to delete?: ")
    while os.path.exists(category_path / recipe) == False:
        print("This recipe does not exist. Please choose a valid recipe.")
        recipe = input("Which recipe would you like to delete?: ")
    if os.path.exists(category_path / recipe):
        os.remove(category_path / recipe)
        print("Recipe has been successfully deleted.")
        input("Press any key to return to main menu")    
    

# 5 - Delete category
## Choose category
## Delete category

def delete_category():
    category = input("Enter the category you would like to delete: ")
    category_path = Path("recipes") / category
    while os.path.isdir(category_path) == False:
        print("This category does not exist. Please choose a valid category.")
        category = input("Enter the category for the recipe you want to delete: ")
        category_path = Path("recipes") / category
    if os.path.exists(category_path):
        os.rmdir(category_path)
        print("Category has been successfully deleted.")
        input("Press any key to return to main menu")

# 6 - Exit

def exit_program():
    exit


# Welcome greeting
# Recipes are in ... folder
# This many recipes are inside the folder
# While loop until exit to keep showing options
# Clean console each time it goes back to options

def main():
    recipes = 0
    play = True
    
    location = Path.absolute(Path("recipes"))
    print("Welcome to your Recipe Manager!")
    print(f"Your recipes are stored here: {location}")
    for d in os.listdir(location):
        if os.path.isdir(os.path.join(location, d)):
            recipes += len(os.listdir(os.path.join(location, d)))
    print(f"You have {recipes} recipes in total.")

    while play == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = print_menu()
        if choice == '1':
            read_recipe()
        elif choice == '2':
            create_recipe()
        elif choice == '3':
            create_category()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            delete_category()
        elif choice == '6':
            play = False
            exit_program()
            
main()
