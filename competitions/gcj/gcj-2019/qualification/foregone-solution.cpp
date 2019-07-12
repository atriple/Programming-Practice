//Status : Accepted !
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int t; scanf("%d\n", &t);
	for (int tc = 1; tc <= t; tc++) {
		int N, A, B;
		string out;
		cin >> N;

		string ns = to_string(N);
		out = ns;

		int i = 0;
		for (int i = 0; i < ns.length(); ++i) {
			if (ns[i] == '4') {
				ns[i] = '2';
				out[i] = '2';
			}
			else out[i] = '0';
		}
		A = stoi(ns);
		B = stoi(out);
		printf("Case #%d: %d %d\n", tc, A, B);
	}
	return 0;
}