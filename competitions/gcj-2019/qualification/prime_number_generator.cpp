// This porgram generates prime numbers and displays them to SDTOUT.
// Written by Mitchell Robinson
// 3 September, 2014
#include <iostream>
#include <cmath>
using namespace std;

int main()
{  
  const unsigned long MAX_SIZE = 20000000;
  bool *numberList = new bool[MAX_SIZE + 1];
  int count = 1; // Used to format how wide the displayed list appears.
  int width = 10; // Number of columns that should be displayed.

  // Omit all odd non-prime numbers.
  for(unsigned long i = 3; i <= sqrt(MAX_SIZE); i += 2)
  {
    for(unsigned long j = i; i * j <= MAX_SIZE; j += 2)
    {
      numberList[i*j] = true;
    }
  }

  // Display prime numbers.
  cout << "2\t"; // Two is the only prime even number.
  for(unsigned long i = 3; i <= MAX_SIZE; i += 2)
  {
    // Display number if element was not set.
    if (!numberList[i])
    {
      cout << i << "\t"; 
      count++;
    }
    
    // Set number of columns in STDOUT.
    if (count == width)
    {
      cout << endl;
      count = 0;
    }
  }
  cout << endl;
  
  return 0;
}
