# Reverse String

Reverse a string

For example:
input: "cool"
output: "looc"

## Notes
Head to 
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods or
- https://www.w3schools.com/js/js_string_methods.asp
For available methods for String in Javascript.

Here's some idea :
- There's no straight reverse method for string in Javascript
- string can be accessed like array in Javascript, but we don't have very short iterator statement like python `str[::-1]`
- Array in Javascript has method reverse though.
- Caranya banyak, bisa imperative dengan looping, recursive, dsb.
- Paling standard(selama dia ASCII) dan singkat pakai `string.split("").reverse().join("");` tapi gua bakal nulis berbagai alternatif metode disini (kalau sempet), kalau ga sempet cek link di bawah.


- Introductory challenge to reverse an input string [https://medium.freecodecamp.org/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb](https://medium.freecodecamp.org/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb)
- Interesting insight about reverse string method in JS https://stackoverflow.com/a/26610963/9310985