#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// myObject.__proto__.incr = function () {
//   this.value += 1;
// };

myObject.incr = function () {
  this.value++;
};

// Object.defineProperty(myObject, 'incr', {
//   get: function () {
//     return function () {
//       this.value++;
//     };
//   }
// });

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
