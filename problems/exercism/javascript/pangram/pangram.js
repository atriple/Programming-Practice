//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'.split('');

export const isPangram = (str) => (ALPHABETS.every((letter) => str.toLowerCase().includes(letter)));