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

export const toRna = (nucleotides) => {
  let complements = '';
  for(let n of nucleotides){
    complements = complements + NUCLEOTIDE_COMPLEMENT[n];
  }
  return complements;
};
