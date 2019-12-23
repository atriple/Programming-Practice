//
// This is only a SKELETON file for the 'Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Triangle {
  constructor(a, b, c) {
    this.sides = [a, b, c];
    this.largestSide = Math.max(...this.sides);
  }

  isTriangle() {
    /*
    Return boolean type, whether it is legal triangle or not
    */

    //Interestingly, triangle inequality rule is enough to check it.
    if(this.largestSide >= this.sides[0] + this.sides[1] + this.sides[2] - this.largestSide) 
      return false;

    return true;
  }

  kind() {
    if(!this.isTriangle()){ throw new Error("This is not triangle!"); }

    const [a, b, c] = this.sides;
    
    //Check equilateral
    if(a == b && a == c) { return 'equilateral';}

    //Check isosceles
    if(a == b || a == c || b == c) { return 'isosceles';}

    return 'scalene';
  }
}
