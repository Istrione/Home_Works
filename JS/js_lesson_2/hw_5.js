// Задание №5 Реализовать четыре основные арифметические операции в виде функций с двумя
//параметрами. Обязательно использовать оператор return.

function sum(a, b) {
    return a + b;
}

function sub(a, b) {
    return a - b;
}

function wor(a, b) {
    return a * b;
}

function div(a, b) {
    return a / b;
}

console.log(`a = 3, b = 5. 
Результат суммы ${sum(3, 5)}, 
Результат вычитания ${sub(3, 5)}, 
Результат произведения ${wor(3, 5)}, 
Результат деления ${div(3, 5)}`);