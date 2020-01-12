/* eslint-disable no-unused-vars */
//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const hey = (message) => {
  if(/^\s*$/.test(message)) return "Fine. Be that way!";
  if(/^[^a-z]*[A-Z]+[^a-z]*\?$/.test(message)) return "Calm down, I know what I'm doing!";
  if(/.*\?\s*$/.test(message)) return "Sure.";
  if(/^[^a-z]*[A-Z]+[^a-z]*$/.test(message)) return "Whoa, chill out!";
  return "Whatever."
};