# Class for holding recipe details
class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

# Class for holding recipes
class RecipeList:
    def __init__(self):
        self.recipes = []
    
    def AddRecipe(self):
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
        
        newRecipe = Recipe(newTitle, newIngredients, newInstructions)
        self.recipes.append(newRecipe)
    
    def ViewAllRecipes(self):
        print("Listing all recipes:")
        for recipe in self.recipes:
            print(recipe.title)
    
    def SearchByTitle(self, titleToSearch):
        SearchRecipeTitle = lambda recipe : recipe.title.lower() == titleToSearch.lower()
        return list(filter(SearchRecipeTitle, self.recipes))
    
    def SearchByIngredient(self, ingredientToSearch):
        listToReturn = []

        for recipe in self.recipes:
            if ingredientToSearch in recipe.ingredients:
                listToReturn.append(recipe)
        
        return listToReturn
    
    def EditRecipe(self, titleToSearch, title, ingredients, instructions):
        # Search for recipe to edit
        matchingRecipe = self.SearchByTitle(titleToSearch)
        recipeToEdit = matchingRecipe[0]

        '''# Ask for new title
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
                i += 1'''
        
        # Change recipe details
        recipeToEdit.title = title
        recipeToEdit.ingredients = ingredients
        recipeToEdit.instructions = instructions

        print("Recipe edited successfully")
    
    def DeleteRecipe(self, titleToSearch):
        matchingRecipe = self.SearchByTitle(titleToSearch)
        recipeToDelete = matchingRecipe[0]
        self.recipes.remove(recipeToDelete)
    
    def SaveToJSON(self):
        pass

    def LoadFromJSON(self):
        pass

def InterpretInput(text, choice):
    if (choice.isnumeric()):
        outputString = ""

        match choice:
            case '1':
                # View all recipes
                pass
            case '2':
                # Add a recipe
                pass
            case '3':
                # Edit recipe
                pass
            case '4':
                # Search by title
                pass
            case '5':
                # Search by ingredient
                pass
            case '6':
                # Delete a recipe
                pass
        
        print(outputString)
    else:
        print("Invalid input. Try again.\n")
        print(text)
        choice = input("Type the number corresponding to the option you want to pick: ")
        InterpretInput(text, choice)

def main():
    #CLI interface
    print("Welcome to the Recipe Manager!")
    options = "Here are your options:\n\n1. View all recipes\n2. Add a recipe\n3. Edit a recipe\n4. Search recipes by title\n5. Search recipes by ingredient\n6. Delete a recipe\n"
    print(options)
    choice = input("Type the number corresponding to the option you want to pick: ")
    InterpretInput(options, choice)

if __name__ == "__main__":
    main()