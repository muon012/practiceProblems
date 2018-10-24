#include <iostream>
using namespace std;

// Requires:
// variables, data types, and numerical operators
// basic input/output
// logic (if statements, switch statements)
// loops (for, while, do-while)
// arrays

// Write a program that asks the user to enter the number of pancakes eaten for breakfast by
// 10 different people (Person 1, Person 2, ..., Person 10)
// Once the data has been entered the program must analyze the data and output which person ate the
// most pancakes for breakfast.

// ★ Modify the program so that it also outputs which person ate the least number of pancakes for breakfast.

// ★★★★ Modify the program so that it outputs a list in order of number of pancakes eaten of all 10 people.
// i.e.
// Person 4: ate 10 pancakes
// Person 3: ate 7 pancakes
// Person 8: ate 4 pancakes
// ...
// Person 5: ate 0 pancakes

int main()
{

    int customers[10]{};   // Array of ten customers whose number of pancakes will be input at their index
    int highest{};         // This is the amount of highest cakes eaten by a customer, we assume it is the first value in the array
    int highestCustomer{1}; // Index of highest, start at 1 for testing purposes.
    int lowest{};          // This will be the amount of least cakes eaten
    int lowestCustomer{1};  // The index of lowest, start at 1 for testing purposes.
    cout << "Enter the amounf of pancakes each person ate:" << endl;
    cout << "Person 1: ";
    cin >> customers[0];
    cout << "Person 2: ";
    cin >> customers[1];
    cout << "Person 3: ";
    cin >> customers[2];
    cout << "Person 4: ";
    cin >> customers[3];
    cout << "Person 5: ";
    cin >> customers[4];
    cout << "Person 6: ";
    cin >> customers[5];
    cout << "Person 7: ";
    cin >> customers[6];
    cout << "Person 8: ";
    cin >> customers[7];
    cout << "Person 9: ";
    cin >> customers[8];
    cout << "Person 10: ";
    cin >> customers[9];

    cout << "[ ";
    for (int i{0}; i < 10; i++)
    {
        cout << customers[i] << " ";
    }
    cout << "]" << endl;

    // Finding the highest value
    highest = customers[0];
    for (int i{1}; i < 10; i++)
    {
        if (highest < customers[i])
        {
            highest = customers[i];
            highestCustomer = i + 1;
        }
    }
    cout << "The highest amount of pancakes(" << highest << ") was eaten by Person " << highestCustomer << endl;

    // Finding the lowest value
    lowest = customers[0];
    for (int i{1}; i < 10; i++)
    {
        if (lowest > customers[i])
        {
            lowest = customers[i];
            lowestCustomer = i + 1;
        }
    }
    cout << "The lowest amount of pancakes(" << lowest << ") was eaten by Person " << lowestCustomer << endl;
    return 0;
}