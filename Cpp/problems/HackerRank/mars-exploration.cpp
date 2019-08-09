// Problems : https://www.hackerrank.com/challenges/mars-exploration/problem
// Solutions by Andi Aqil Amanulhaq

#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;

	const string sos = "SOS";

	for (int i = 1; i <= t; ++i) {
		string s;
		int count = 0;

		cin >> s;

		for (int i = 0; i < s.length(); ++i) {
			if (s[i] != sos[i % 3]) count++;
		}

		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}