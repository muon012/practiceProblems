#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    vector<string> problems{"Grading Program", "Cola Machine", "While( user == gullible )", "Pancake Glutton"};
    int iterator {};
    for(auto elem: problems){
        iterator += 1;
        cout << iterator << ") " << elem << endl;
    }
    return 0;
}