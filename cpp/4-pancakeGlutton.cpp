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
    const int num_of_customers{10}; // Number of costumers;
    int customers_pancakes[10][2]{ {1, 0}, {2, 0}, {3, 0}, {4, 0}, {5, 0}, {6, 0}, {7, 0}, {8, 0}, {9, 0}, {10, 0}}; // 2D-array representing each customer and the number of pancakes each ate;
    int winner_customer{}; // This represents the index of the customer with the highest/lowest amount of pancakes;
    cout << "Enter how many pancakes each cumstomer ate: " << endl;

    for(int i{}; i < num_of_customers; i++){
        cout << "Customer " << customers_pancakes[i][0] << ": ";
        cin >> customers_pancakes[i][1];
    }

    // Finding the highest value
    int highest = customers_pancakes[0][0];
    for (int i{0}; i < num_of_customers; i++)
    {
        if (highest < customers_pancakes[i][1])
        {
            highest = customers_pancakes[i][1];
            winner_customer = customers_pancakes[i][0];
        }
    }
    cout << "The highest amount of pancakes(" << highest << ") was eaten by Person " << winner_customer << endl;

    // Finding the lowest value
    int lowest = customers_pancakes[0][0];
    for (int i{0}; i < num_of_customers; i++)
    {
        if (lowest > customers_pancakes[i][1])
        {
            lowest = customers_pancakes[i][1];
            winner_customer = customers_pancakes[i][0];
        }
    }
    cout << "The lowest amount of pancakes(" << lowest << ") was eaten by Person " << winner_customer << endl;


    // Sorting the array
    int customer_number{}; // Making a temporary variable to store the value of the customer's number;
    int customer_pancake_number{}; // Making a temporary variable to store the value of the customer's amount of pancakes eaten;

    for (int i{}; i < num_of_customers - 1; i++)
    {
        for (int j{}; j < num_of_customers - 1 - i; j++)
        {
            if (customers_pancakes[j][1] > customers_pancakes[j + 1][1])
            {
                customer_number = customers_pancakes[j][0];
                customer_pancake_number = customers_pancakes[j][1];
                customers_pancakes[j][0] = customers_pancakes[j + 1][0];
                customers_pancakes[j][1] = customers_pancakes[j + 1][1];
                customers_pancakes[j + 1][0] = customer_number;
                customers_pancakes[j + 1][1] = customer_pancake_number;
            }
        }
    }

    cout << "A list of the customers in ascending order by number of pancakes eaten." << endl;
    
    for (int i{}; i < num_of_customers; i++)
    {
        cout << "Person " << customers_pancakes[i][0] << " ate: " << customers_pancakes[i][1] << " pancakes." << endl;
    }

    return 0;
}