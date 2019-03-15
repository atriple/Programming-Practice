/*
Problems :
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
*/
#include<iostream>

int main() {
	int sum = 0;

	//Fibonacci term
	int term1 = 1, term2 = 1, term3 = term1 + term2;
	

	while (!(term3 > 4 * 1000000)) {
		if (term3 % 2 == 0) {
			std::cout << term3 << std::endl;
			sum += term3;
		}
		term1 = term2;
		term2 = term3;
		term3 = term1 + term2;
	}

	std::cout << sum << std::endl;
	system("pause");
	
	return 0;
}