import json

# Class for holding recipe details
class Recipe:
    # Initialise recipe with title as string, ingredients and instructions as lists
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

# Class for holding recipes
class RecipeList:
    # Initialise recipe list as a list that will hold recipes
    def __init__(self):
        self.recipes = []
    
    # Method to create a new recipe and add it to the recipe list
    def AddRecipe(self):
        # Ask for new title
        newTitle = input("\nInput the new title: ")

        # Ask for new ingredients
        # First ask for how many ingredients to add
        newIngredients = []
        numOfIngredients = input("How many ingredients to add? ")
        # Repeat question if input was not numeric, else iteratively ask user to input ingredients
        if not numOfIngredients.isnumeric():
            while not numOfIngredients.isnumeric():
                numOfIngredients = input("We need a numeric input. How many ingredients to add? ")
        else:
            print(f"Adding {numOfIngredients} ingredients: ")
            for i in range(0,int(numOfIngredients)):
                newItemtoAdd = input("Input ingredient to add: ")
                newIngredients.append(newItemtoAdd)
                i += 1

        # Ask for new instructions
        # First ask for how many instructions to add
        newInstructions = []
        numOfInstructions = input("How many instructions in the recipe? ")
        # Repeat question if input was not numeric, else iteratively ask user to input instructions
        if not numOfInstructions.isnumeric():
            while not numOfInstructions.isnumeric():
                numOfInstructions = input("We need a numeric input. How many instructions in the recipe? ")
        else:
            print(f"Adding {numOfInstructions} instructions: ")
            for i in range(0,int(numOfInstructions)):
                newItemtoAdd = input("Input instruction to add: ")
                newInstructions.append(newItemtoAdd)
                i += 1
        
        # Create new Recipe object with details provided by user and append it to recipe list
        newRecipe = Recipe(newTitle, newIngredients, newInstructions)
        self.recipes.append(newRecipe)
    
    # Method to view all recipes
    def ViewAllRecipes(self):
        # For loop to iterate through all recipes in recipe list and print the title
        print("\nListing all recipes:")
        for recipe in self.recipes:
            print(recipe.title)
    
    # Method to search for a recipe by title
    def SearchByTitle(self):
        # Retrieve input and use lambda to check if any recipe titles in recipe list match the input
        titleToSearch = input("\nEnter the name of the recipe to search for: ")
        SearchRecipeTitle = lambda recipe : recipe.title.lower() == titleToSearch.lower()
        results = list(filter(SearchRecipeTitle, self.recipes))
        # Print all results found
        for result in results:
            print(result.title)
    
    # Method to search for a recipe by title
    def SearchByIngredient(self):
        # Retrieve input and use for loop to check if the ingredient given as input is in
        # any of the ingredient lists in any of the recipes in recipe list
        ingredientToSearch = input("\nEnter the name of the ingredient: ")
        results = []

        for recipe in self.recipes:
            if ingredientToSearch in recipe.ingredients:
                results.append(recipe.title)
        
        # Print all results found
        for result in results:
            print(result)
    
    def EditRecipe(self):
        # Search for recipe to edit
        titleToSearch = input("\nEnter the name of the recipe to edit:")
        for recipe in self.recipes:
            if titleToSearch.lower() == recipe.title.lower():
                # Ask for new title
                newTitle = input("Input the new title: ")

                # Ask for new ingredients
                # First ask for how many ingredients to add
                newIngredients = []
                numOfIngredients = input("How many ingredients to add? ")
                # Repeat question if input was not numeric, else iteratively ask user to input ingredients
                if not numOfIngredients.isnumeric():
                    while not numOfIngredients.isnumeric():
                        numOfIngredients = input("We need a numeric input. How many ingredients to add? ")
                else:
                    print(f"Adding {numOfIngredients} ingredients: ")
                    for i in range(0,int(numOfIngredients)):
                        newItemtoAdd = input("Input ingredient to add: ")
                        newIngredients.append(newItemtoAdd)
                        i += 1

                # Ask for new instructions
                # First ask for how many instructions to add
                newInstructions = []
                numOfInstructions = input("How many instructions in the recipe? ")
                # Repeat question if input was not numeric, else iteratively ask user to input instructions
                if not numOfInstructions.isnumeric():
                    while not numOfInstructions.isnumeric():
                        numOfInstructions = input("We need a numeric input. How many instructions in the recipe? ")
                else:
                    print(f"Adding {numOfInstructions} instructions: ")
                    for i in range(0,int(numOfInstructions)):
                        newItemtoAdd = input("Input instruction to add: ")
                        newInstructions.append(newItemtoAdd)
                        i += 1
                
                # Change recipe details
                recipe.title = newTitle
                recipe.ingredients = newIngredients
                recipe.instructions = newInstructions

                print("Recipe edited successfully")
            else:
                print("No recipe matching that title was found")
    
    # Method to delete recipe
    def DeleteRecipe(self):
        # Retrieve input and use for loop to iterate through recipe list
        titleToSearch = input("\nEnter name of recipe to delete: ")
        for recipe in self.recipes:
            # If matching recipe title is found then remove it from recipe list
            if titleToSearch.lower() == recipe.title.lower():
                self.recipes.remove(recipe)
        print("Recipe deleted")
    
    # Method to save recipe list as json
    def SaveToJSON(self):
        # Turn existing recipes into dicts and put them in a list
        jsonRecipeList = []
        for recipe in self.recipes:
            jsonRecipe = {'title': recipe.title, 'ingredients': recipe.ingredients, 'instructions': recipe.instructions}
            jsonRecipeList.append(jsonRecipe)
        
        # Turn the whole list into a json object and store it as a json file
        jsonObject = json.dumps(jsonRecipeList)
        
        with open("data/recipes.json", "w") as outfile:
            outfile.write(jsonObject)

    # Method to load recipe list from a json file
    def LoadFromJSON(self):
        # Open the json file
        with open("data/recipes.json", "r") as openfile:
            jsonRecipeList = json.load(openfile)

        # For each recipe in the json file, instantiate it as a Recipe class object and append it to
        # the recipe list
        for recipe in jsonRecipeList:
            recipe = Recipe(recipe['title'], recipe['ingredients'], recipe['instructions'])
            self.recipes.append(recipe)

# Fuction to interpret user input and execute functions based on said input
def InterpretInput(recipeList, text, choice):
    if (choice.isnumeric()):
        outputString = ""

        match choice:
            case '1':
                # Save recipes
                recipeList.SaveToJSON()
                print("File saved to data/recipes.json successfully!")
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '2':
                # Load recipe
                recipeList.LoadFromJSON()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '3':
                # View all recipes
                recipeList.ViewAllRecipes()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '4':
                # Add a recipe
                recipeList.AddRecipe()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '5':
                # Edit recipe
                recipeList.EditRecipe()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '6':
                # Search by title
                recipeList.SearchByTitle()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '7':
                # Search by ingredient
                recipeList.SearchByIngredient()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '8':
                # Delete a recipe
                recipeList.DeleteRecipe()
                entrToCont = input("Press ENTER to continue: ")

                print(text)
                choice = input("Type the number corresponding to the option you want to pick: ")
                InterpretInput(recipeList, text, choice)
            case '9':
                print("Exiting program")
        
        print(outputString)
    else:
        print("Invalid input. Try again.\n")
        print(text)
        choice = input("Type the number corresponding to the option you want to pick: ")
        InterpretInput(recipeList, text, choice)

def main():
    #CLI interface
    print("Welcome to the Recipe Manager!")
    options = "Here are your options:\n\n1. Save Recipes\n2. Load Recipes\n3. View all recipes\n4. Add a recipe\n5. Edit a recipe\n6. Search recipes by title\n7. Search recipes by ingredient\n8. Delete a recipe\n9. Exit"
    print(options)
    choice = input("Type the number corresponding to the option you want to pick: ")
    recipeList = RecipeList()
    InterpretInput(recipeList, options, choice)

if __name__ == "__main__":
    main()