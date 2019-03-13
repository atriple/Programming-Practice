#include <iostream>
#include <cstdio>

//Problems : Multiples of 3 and 5

int main() {
	int i = 0;
	int sum = 0;
	while (i < 1000) {
		if (i % 3 == 0 || i % 5 == 0) sum += i;
		i++;
	};

	std::cout << sum;

	int placehold;
	std::cin >> placehold;
	return 0;
}
