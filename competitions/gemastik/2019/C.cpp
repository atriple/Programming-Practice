// WIP
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int i, j, m;
	//input matrix
	cin >> i;
	cin >> j;
	cin >> m;
	vector<vector<int>> arah(j + 2, vector<int>(j+2));

	for (int k = 0; k <= j + 1; k++) {
		for (int h = 0; h <= j + 1; h++) {
			cin >> arah[k][h];
			if (arah[h][k])
		}
	}
	
	cout << i << endl;
	cout << j << endl;
	cout << m << endl;
}