//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isPangram = (str) => {
  let pangram = true;

  //Generate object {a : false, b : false, ..., z: false}, I'm not sure if this is a good practice...
  let LETTER_CHECKLIST = 'abcdefghijklmnopqrstuvwxyz'.split('').reduce(
    (list = {}, alphabet) => {
      list[alphabet] = false;
      return list;
    }, {});
  
  //Check
  str.toLowerCase().split('').map((ch) => {
      if (LETTER_CHECKLIST[ch] == false) LETTER_CHECKLIST[ch] = true;
    });

  for(let key in LETTER_CHECKLIST){
    if (LETTER_CHECKLIST[key] == false) pangram = false;
  }

  return pangram;
};
