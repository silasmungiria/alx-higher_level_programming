#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// This line outputs the initial content of the "myObject" to the console.

myObject.incr = function () {
  // This line adds a method named "incr" to the "myObject".
  this.value++;
  // This method increments the value of "value" property of "myObject" by 1
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
