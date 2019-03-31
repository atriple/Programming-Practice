//inputformat.cpp but cleaner (copy-paste ready)
#include <iostream> 
#include <vector>

using namespace std; 


int main() {
	/////////////////////////////////////////////////////////////////////////////////////
	//Option #1, this one is pretty simple, found it from GCJ.
	//start copy here
	int t, n, m;
	cin >> t; //number of case input

	int output[t];
	
	//Case Input Loop
	for (int i = 0; i < t; ++i) {
		cin >> n >> m; 
		cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;

		output[t] = 1; 
	}

	//Loop for ouptut
	for (int i = 0; i < t; i++) {
		cout << output[t] << endl; 
	}
	//endcopy here
	/////////////////////////////////////////////////////////////////////////////////////

	//Option #2, HackerRank Format, looks a bit unfamiliar at first but I think there's  good reason for it.
	//It usually use multiple function (usually 1 function to process from input to the output).


	/////////////////////////////////////////////////////////////////////////////////////

	//Array Input is used to read line of numbers, this used a lot in Competitive Programming
	//Array Input Option #1


	return 0;
}