// Problems : https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
// Solutions by Andi Aqil A

#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;

	const string hr = "hackerrank";

	for (int i = 1; i <= t; ++i) {
		int idx = 0;
		int truth_level = 0;
		string output = "NO";

		while (idx < s.length()) {
			if (s[idx] == hr[truth_level]) {
				truth_level++;
			}

			if (truth_level == hr.length()) output = "YES";
			idx++;
		}
		cout << output << endl;
	}
	return 0;
}