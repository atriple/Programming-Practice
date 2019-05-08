/*
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number 
and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.
*/

for (var i = 1; i <= 100; i++){
    var text = "";
    if (i % 3 == 0){
        text = text + "Fizz";
    }

    if (i % 5 == 0){
        text = text + "Buzz";
    }

    if(text != "")
    console.log(text);
    else console.log(i);
}