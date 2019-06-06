#include <iostream>
#include <string>

using namespace std;

int main() {
	string s = "aba";
	int length = s.length();
	int n = 10;
	int full_a = 0; //jumlah a secara total di unit string
	int slice_a = 0; 

	//find all a in unit string s
	for (char i : s) {
		if (i == 'a') full_a++;
	}

	// total pengulangan komplit, you actually can write it straight to formula rather than wrap it to variable like this
	int fullRepeat = n / length; 
	//jika n < |s|, maka full_repeat = 0, jadi cuma dilihat bagian sisa saja


	//Bagian sisa
	for (int j = 0; j < n % length; j++) { 
		if (s[j] == 'a') slice_a++;
	}

	int total_a = (fullRepeat * full_a) + slice_a;

	/*
	We can actually done this without separating count_a value, it can reduce the memory space at least.
	1. Process the fullRepeat * full_a first (which is going to be count_a)
	2. Then do the slice_a loops, but instead of adding slice_a++, we can use count_a instead.
	*/

	cout << total_a << endl;

	return 0;
}