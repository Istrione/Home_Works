// Задание №8 С помощью рекурсии организовать функцию возведения числа в степень. Формат: function
//power(val, pow), где val — заданное число, pow –— степень.

function power(val, pow) {
    if (val == 0){
        return 0;
    } else if (pow == 0){
        return 1;
    } else if (pow < 0){
        return power(1/val, -pow);
    } else {
        return val * power(val, pow - 1);
    }
}

console.log(power(10, -2))