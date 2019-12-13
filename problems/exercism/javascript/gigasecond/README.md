# Gigasecond

Given a moment, determine the moment that would be after a gigasecond
has passed.

A gigasecond is 10^9 (1,000,000,000) seconds.

## Notes
In this problems, we learn about Javascript `Date`. Here's good reference for it https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date

Here's some quickie :
- `Date.UTC(Year, MonthIndex, Day)` : generate UTC number (integer milisecond after UNIX epoch).
- `Date.parse(dateString)` : parse string of date in this format http://www.ecma-international.org/ecma-262/5.1/#sec-15.9.1.15
- `Date.prototype.getTime()` : turn instance of Date into value in UTC number.
    - Awalnya gua pake `valueOf()`, tapi ternyata lebih baik pake `getTime()` walaupun ngereturn nilai yang sama. Karena `valueOf()` itu method yg ada di semua objek yang bisa kita override untuk ngereturn nilai lain.
- We can use scientific notation to express number in Javascript. Since Javascript use millisecond as epoch time, then we have to converse 10^9 s to 10^12 ms
- For cleaner code, **you should name the CONSTANT**, by convention using capital letter.


## Source
### tentang getTime() dan valueOf()
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime 
- https://stackoverflow.com/questions/9710136/in-javascript-why-do-date-objects-have-both-valueof-and-gettime-methods-if-they

### From exercism
Chapter 9 in Chris Pine's online Learn to Program tutorial. [http://pine.fm/LearnToProgram/?Chapter=09](http://pine.fm/LearnToProgram/?Chapter=09)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have
completed the exercise.
