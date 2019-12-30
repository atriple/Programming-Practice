export class Matrix {
  constructor(matrixString) {
    this.matrix = matrixString.split('\n').map(row => row.split(' ').map(item => Number(item)));
    this.transpose = this.matrix[0].map((col, idx) => this.matrix.map(row => row[idx])); 
  }

  get rows() {
    return this.matrix;
  }

  get columns() {
    return this.transpose;
  }
}
