#!/usr/bin/node
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < size; i++) {
    square += '\n';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
  }
  console.log(square);
}
