//Status : Accepted, I think it can solve hidden case too.
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int t; scanf("%d\n", &t);
	for (int tc = 1; tc <= t; tc++) {
		int N;
		string lydia;
		cin >> N;
		cin >> lydia;

		string us = lydia;

		for (int i = 0; i < (2 * N - 2); i++) {
			if (lydia[i] == 'E') {
				us[i] = 'S';
			}
			else us[i] = 'E';
		}
		cout << "Case #" << tc << ": " << us << endl;
	}
	return 0;
}