//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const GIGAMILLISEC = 1e12; // 10^9 sec --> 10^12 ms 

export const gigasecond = (date) => new Date(date.getTime() + GIGAMILLISEC);
