#include<iostream>
using namespace std;

int main()
{
	int n{};
    int temp{};
	cout<<"Enter total number of elements :";
	cin >> n;
	int arr[n];
	cout << "Enter "<< n <<" numbers :";
	for(int i{}; i < n; i++)
	{
		cin >> arr[i];
	}
	cout << "Sorting array using bubble sort technique...\n";
	for(int i{}; i < (n - 1); i++)
	{
		for(int j{}; j < (n - 1 - i); j++)
		{
			if(arr[j] > arr[j+1])
			{
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	cout << "Elements sorted successfully..!!\n";
	cout << "Sorted list in ascending order :\n";
	for(int i{}; i < n; i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}