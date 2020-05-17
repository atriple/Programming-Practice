#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t, N, K, number, countdown, numberOfCountdown = 0;
    vector<int> numbers;
    cin >> t; // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> N >> K;
        countdown = K;
        for(int i = 0; i < N; i++){
            cin >> number;
            numbers.push_back(number);
        }

        for(auto n : numbers){
            cout << n << " ";
            if(n == countdown){
                countdown--;
            }
            else{
                countdown = K;
            }
            
            if(countdown == 0){
                numberOfCountdown++;
                countdown = K;
            }
        }
        cout << "Case #" << i << ": " << numberOfCountdown << endl;

        numbers.clear();
        numberOfCountdown = 0;
      }
    return 0;
}