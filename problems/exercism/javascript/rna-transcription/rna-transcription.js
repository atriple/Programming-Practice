//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const NUCLEOTIDE_COMPLEMENT = {
  'G' : 'C',
  'C' : 'G',
  'T' : 'A',
  'A' : 'U'
};

//Functional Solution
const complement = (n) => NUCLEOTIDE_COMPLEMENT[n];

export const toRna = (nucleotides) => nucleotides.split('').map(complement).join('');
// We can also use reduce() instead of join(), but keep it simple, stupid.

//Initial Solution
// export const toRna = (nucleotides) => {
//   let complements = '';
//   for(let n of nucleotides){
//     complements = complements + NUCLEOTIDE_COMPLEMENT[n];
//   }
//   return complements;
// };