#include<vector>
#include<set>
#include<iostream>

using namespace std;

int main() {
	set<char> x = { 'A', 'B', 'C' };

	auto it = x.begin();
	int size = x.size();
	cout << *it << endl;
	cout << size << endl;

	return 0;
}