//
// This is only a SKELETON file for the 'Collatz Conjecture' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

//RECURSIVE SOLUTION
export const steps = (startNumber) => {
  if(startNumber <= 0) throw new Error('Only positive numbers are allowed');
  if (startNumber === 1) return 0;

  return 1 + steps(startNumber % 2 == 0 ? startNumber/2 : startNumber * 3 + 1);
};
