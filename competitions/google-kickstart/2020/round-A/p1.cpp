#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int t, numberOfHouse, budget, unitPrice, totalPrice = 0, houseCount = 0;
    vector<int> prices;
    cin >> t;

    for(int i = 1; i <= t; ++i) {
        //Input
        cin >> numberOfHouse >> budget;
        for(int i = 0; i < numberOfHouse; ++i){
            cin >> unitPrice;
            prices.push_back(unitPrice);
        }

        //Process
        sort(prices.begin(), prices.end());
        for(auto price : prices){
            totalPrice += price;
            if(totalPrice > budget) break;
            houseCount++;
        }
        
        //Output
	    cout << "Case #" << i << ": " << houseCount << endl;
        
        //Clear Condition
        prices.clear();
        houseCount = 0;
        totalPrice = 0;
    }

    return 0;
}