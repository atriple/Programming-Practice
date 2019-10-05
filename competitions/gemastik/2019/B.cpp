#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>

using namespace std;

int main() {
	string input;
	getline(cin, input);
	istringstream buf(input);
	istream_iterator<string> beg(buf), end;
	vector<string> tokens(beg, end);

	int total = 0;
	int count = 0;

	for (string& s : tokens) {
		total += stoi(s);
		count++;
	}

	if (total % count == 0) {
		cout << "MUNGKIN";
	}
	else {
		cout << "MUSTAHIL";
	}
}