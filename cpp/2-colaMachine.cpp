#include <iostream>
using namespace std;

// Requires:
// variables, data types, and numerical operators
// basic input/output
// logic (if statements, switch statements)

// Write a program that presents the user w/ a choice of your 5 favorite beverages 
// (Coke, Water, Sprite, ... , Whatever).
// Then allow the user to choose a beverage by entering a number 1-5.
// Output which beverage they chose.

// ★ If you program uses if statements instead of a switch statement, modify it to use a switch statement.
// If instead your program uses a switch statement, modify it to use if/else-if statements.

// ★★ Modify the program so that if the user enters a choice other than 1-5 then it will 
// output "Error. choice was not valid, here is your money back."

int main(){
    
    int choice{}; // Customer's choice

    do{
        cout << "Choose your beverage (Press 0 to exit): " << endl;
        cout << "1 - Coke" << endl;
        cout << "2 - Root Beer" << endl;
        cout << "3 - Sprite" << endl;
        cout << "4 - Fanta" << endl;
        cout << "5 - Gatorade" << endl;
        cin >> choice;
        switch(choice){
            case 1: cout << "You chose Coke." << endl;
            break;
            case 2: cout << "You chose Root Beer." << endl;
            break;
            case 3: cout << "You chose Sprite." << endl;
            break;
            case 4: cout << "You chose Fanta." << endl;
            break;
            case 5: cout << "You chose Gatorade." << endl;
            break;
            default: cout << "Error. choice was not valid, here is your money back." << endl;
        }
    }while(choice != 0);

    return 0;
}