// 1. Functions of Integers on Cartesian Plane 		
// Evan McGann - 6/22/2016

function sumin(n) {
  return n <= 1 ? 1 : Math.pow(n, 2) + sumin(n - 1);
}

function sumax(n) {
  return n <= 1 ? 1 : sumax(n - 1) + 2 * Math.pow(n, 2) - n;
}

function sumsum(n) {
  return sumin(n) + sumax(n);
}

function sumsum2(n) {
  return n <= 0 ? 0 : 2 * n * range(1, n + 1).reduce(function (p, c) { return p + c; });
}

function range(start, end) {
  return Array.apply(null, Array(end - start)).map(function (_, i) { return i + start; });
}