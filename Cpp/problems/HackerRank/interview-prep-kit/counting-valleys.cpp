//Algorithm Analysis : Given String input with length n, time complexity is O(n).

#include <iostream>
#include <string>

using namespace std;


int main() {
	int sea_level = 0; // we always start from flat 0
	int countValley = 0; // desired output
	string x = "UDDDUDUU"; //input commands
	bool below = false; //check whether we currently below sea level or not.


	//We can iterate string with foreach, since string itself is array of char.
	for (char i : x) {
		if (i == 'U') sea_level++;
		else sea_level--;

		if (sea_level == 0) below = false; 

		if (sea_level < 0 && below == false) {
			countValley++;
			below = true;
		}
	}

	cout << countValley << endl;

	system("pause");

	return 0;

}