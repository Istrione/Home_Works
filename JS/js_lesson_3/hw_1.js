// Задание №1 С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

let max = 100;
let n = 2;
let primeArr = [];

while (n <= max) {
    if (n == 2 || n == 3 || n == 5 || n == 7) {
        primeArr.push('' + n);
        n++;
        continue;
    } else if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0) {
        n++;
        continue;
    }
    primeArr.push('' + n++);
} 

console.log(primeArr)