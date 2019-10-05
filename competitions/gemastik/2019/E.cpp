#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	int output = 0; //jumlah match
	cin >> N;

	vector<int> panjang(N);
	vector<int> lebar(N);

	int pos[4];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> pos[j];
		}
		//Evaluate pos to panjang lebar
		lebar[i] = pos[2] - pos[0];
		panjang[i] = pos[3] - pos[1];
	}

	//O(n^2) looping check
	for (int k = 0; k < N; k++) {
		for (int w = 0; w < N; w++) {
			if (w == k) continue;
			if (lebar[k] <= lebar[w] && panjang[k] <= panjang[w]) continue;
			if (lebar[k] <= panjang[w] && panjang[k] <= lebar[w]) continue;
			if (lebar[w] <= lebar[k] && panjang[w] <= panjang[k]) continue;
			if (lebar[w] <= panjang[k] && panjang[w] <= lebar[k]) continue;
			output++;
		}
	};

	cout << output/2; //fu**ing combinatorics

	return 0;
}