// Задание №6 Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
//где arg1, arg2 — значения аргументов, operation — строка с названием операции. В
//зависимости от переданного значения выполнить одну из арифметических операций
//(использовать функции из пункта 5) и вернуть полученное значение (применить switch).

function mathOperation(arg1, arg2, operation) {
    
    switch(operation) {
        case 'sum':
            return arg1 + arg2;
            break;
        case 'subtraction':
            return arg1 - arg2;
            break;
        case 'multiplication':
            return arg1 * arg2;
            break;
        case 'division':
            return arg1 / arg2;
            break;
    }
}

console.log(mathOperation(10, 5, 'division'))