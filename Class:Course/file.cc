#include <iostream>
#include <limits>
#include <map>
#include <string>

using namespace std;

void displayRecipeBook(const map<string, string>& recipes) {
    cout << "Recipe Book\n";
    cout << "---------------------------\n";
    for (const auto& pair : recipes) {
        cout << pair.first << ": " << pair.second << endl;
    }
    cout << "---------------------------\n";
}

void addRecipe(map<string, string>& recipeBook) {
    string recipeName, recipeSteps;
    cout << "Enter recipe name: ";
    getline(cin, recipeName);
    cout << "Enter recipe steps: ";
    getline(cin, recipeSteps);
    recipeBook[recipeName] = recipeSteps;
    cout << "Recipe added successfully!\n";
}

void viewRecipe(const map<string, string>& recipeBook, const string& recipeName) {
    auto it = recipeBook.find(recipeName);
    if (it != recipeBook.end()) {
        cout << "Recipe: " << recipeName << endl;
        cout << it->second << endl;
    } else {
        cout << "Recipe not found.\n";
    }
}

int main() {
    map<string, string> recipeBook;

    int choice;
    string recipeName;

    do {
        cout << "\nSelect an option:\n";
        cout << "1. View Recipe Book\n";
        cout << "2. Add Recipe\n";
        cout << "3. View Recipe\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";

        while (!(cin >> choice)) {
            cout << "Invalid input. Please enter a number.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        switch (choice) {
            case 1:
                displayRecipeBook(recipeBook);
                break;
            case 2:
                addRecipe(recipeBook);
                break;
            case 3:
                cout << "Enter recipe name: ";
                getline(cin, recipeName);
                viewRecipe(recipeBook, recipeName);
                break;
            case 4:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
        }

    } while (choice != 4);

    return 0;
}