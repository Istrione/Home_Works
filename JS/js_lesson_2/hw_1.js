// Задание №1 Почему код дает именно такие результаты?

var a = 1, b = 1, c, d;
c = ++a; console.log(c); // 2 
d = b++; console.log(d); // 1
c = (2+ ++a); console.log(c); // 5
d = (2+ b++); console.log(d); // 4
console.log(a); // 3
console.log(b); // 3