#include <iostream>
#include <unordered_map>

using namespace std;

/*
Idea :
It has similar to count the frequency table of data using unordered map
With some additional process, when a data frequency divisible by 2, we count it as a pair.
*/

int main() {
	int pairCount = 0;
	unordered_map<int, int> test;
	vector<int> x = { 10, 20, 20, 10, 10, 30, 50, 10, 20 };

	//for each loop, to add frequency distribution of list x
	for (int i : x) {
		test[i]++; // using [] operator to referencing map key, we put the value as the frequency

		if (test[i] % 2 == 0) {
			pairCount++;
		}
	}
	cout << "Freq of 10 is " << test[10] << endl;
	cout << pairCount << endl;

	system("pause");

	return 0;
}