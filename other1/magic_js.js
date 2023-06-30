const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (n) => {
  const matrix = [];
  let sum = 0;

  for (let i = 0; i < n; i++) {
    matrix.push(readLineAsNumbers());
    sum += matrix[i][i];
  }

  let isMagic = true;

  for (let i = 0; i < n; i++) {
    let rowSum = 0;
    let colSum = 0;

    for (let j = 0; j < n; j++) {
      rowSum += matrix[i][j];
      colSum += matrix[j][i];
    }

    if (rowSum !== sum || colSum !== sum) {
      isMagic = false;
      break;
    }
  }

  console.log(isMagic ? 'YES' : 'NO');

  rl.close();
});

function readLineAsNumbers() {
  return readlineSync
    .question('')
    .trim()
    .split(' ')
    .map(Number);
}
