from dataclasses import dataclass, asdict
import json

# Class for holding recipe details
@dataclass
class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

# Class for holding recipes
@dataclass
class RecipeList:
    def __init__(self):
        self.recipes = []
    
    def AddRecipe(self):
        # Ask for new title
        newTitle = input("\nInput the new title: ")

        # Ask for new ingredients
        newIngredients = []
        numOfIngredients = input("How many ingredients to add? ")
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
        newInstructions = []
        numOfInstructions = input("How many instructions in the recipe? ")
        if not numOfInstructions.isnumeric():
            while not numOfInstructions.isnumeric():
                numOfInstructions = input("We need a numeric input. How many instructions in the recipe? ")
        else:
            print(f"Adding {numOfInstructions} instructions: ")
            for i in range(0,int(numOfInstructions)):
                newItemtoAdd = input("Input instruction to add: ")
                newInstructions.append(newItemtoAdd)
                i += 1
        
        newRecipe = Recipe(newTitle, newIngredients, newInstructions)
        self.recipes.append(newRecipe)
    
    def ViewAllRecipes(self):
        print("\nListing all recipes:")
        for recipe in self.recipes:
            print(recipe.title)
    
    def SearchByTitle(self):
        titleToSearch = input("\nEnter the name of the recipe to search for: ")
        SearchRecipeTitle = lambda recipe : recipe.title.lower() == titleToSearch.lower()
        results = list(filter(SearchRecipeTitle, self.recipes))
        for result in results:
            print(result.title)
    
    def SearchByIngredient(self):
        ingredientToSearch = input("\nEnter the name of the ingredient: ")
        results = []

        for recipe in self.recipes:
            if ingredientToSearch in recipe.ingredients:
                results.append(recipe.title)
        
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
                newIngredients = []
                numOfIngredients = input("How many ingredients to add? ")
                if not numOfIngredients.isnumeric():
                    while not numOfIngredients.isnumeric():
                        numOfIngredients = input("We need a numeric input. How many ingredients to add? ")
                else:
                    print(f"Adding {numOfIngredients} ingredients: ")
                    for i in range(1,numOfIngredients):
                        newItemtoAdd = input("Input ingredient to add: ")
                        newIngredients.append(newItemtoAdd)
                        i += 1

                # Ask for new instructions
                newInstructions = []
                numOfInstructions = input("How many instructions in the recipe? ")
                if not numOfInstructions.isnumeric():
                    while not numOfInstructions.isnumeric():
                        numOfInstructions = input("We need a numeric input. How many instructions in the recipe? ")
                else:
                    print(f"Adding {numOfInstructions} instructions: ")
                    for i in range(1,numOfInstructions):
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
    
    def DeleteRecipe(self):
        titleToSearch = input("\nEnter name of recipe to delete: ")
        for recipe in self.recipes:
            if titleToSearch.lower() == recipe.title.lower():
                self.recipes.remove(recipe)
        print("Recipe deleted")
    
    def SaveToJSON(self):
        jsonRecipeList = []
        for recipe in self.recipes:
            jsonRecipe = {'title': recipe.title, 'ingredients': recipe.ingredients, 'instructions': recipe.instructions}
            jsonRecipeList.append(jsonRecipe)
        
        jsonObject = json.dumps(jsonRecipeList)
        
        with open("data/recipes.json", "w") as outfile:
            outfile.write(jsonObject)

    def LoadFromJSON(self):
        #jsonRecipeList = [{"title": "asfd", "ingredients": ["as"], "instructions": ["asdf"]}, {"title": "asfd", "ingredients": ["asfdg", "d"], "instructions": ["wefgrfs", "rafds", "fra"]}]
        with open("data/recipes.json", "r") as openfile:
            jsonRecipeList = json.load(openfile)

        for recipe in jsonRecipeList:
            recipe = Recipe(recipe['title'], recipe['ingredients'], recipe['instructions'])
            self.recipes.append(recipe)

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