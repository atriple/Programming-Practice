#include <iostream> // includes cin to read from stdin and cout to write to stdout
#include <vector>

using namespace std; // since cin and cout are both in namespace std, this saves some text

//There's several format that you can use for C++
int main() {
	/////////////////////////////////////////////////////////////////////////////////////
	//Option #1, this one is pretty simple, found it from GCJ.
    int t, n, m;
    cin >> t; // Input how many case
    
	//If you have multiple case, we can save the outputs in array so we can print it later.
	//most of the time, the output will be produced after all cases inputs
	int output[t];

    //Loop per case.
    for (int i = 0; i < t; ++i) { 
		//Just extra notes we strictlty begin with i=0, not 1, just because we want to put the output into array
		cin >> n >> m; // read n and then m, this is example for 2 integer input.
		cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    
		output[t] = 1; //save the results to output.
    }

	//Loop for ouptut, most of the time, the output will be produced after all cases inputs
	for (int i = 0; i < t; i++) {
		cout << output[t] << endl; //Depend on the problems, you might not use endl(new line).
	}

	/////////////////////////////////////////////////////////////////////////////////////

	//Option #2, HackerRank Format, looks a bit unfamiliar at first but I think there's  good reason for it.
	//It usually use multiple function (usually 1 function to process from input to the output).


	/////////////////////////////////////////////////////////////////////////////////////

	//Array Input is used to read line of numbers, this used a lot in Competitive Programming
	//Array Input Option #1


      return 0;
    }