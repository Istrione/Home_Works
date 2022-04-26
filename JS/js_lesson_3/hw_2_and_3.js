// Задание №2 С этого урока начинаем работать с функционалом интернет-магазина. Предположим, есть
//сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в
//зависимости от находящихся в ней товаров.

// Задание №3 Товары в корзине хранятся в массиве. Задачи:
//a. Организовать такой массив для хранения товаров в корзине;
//b. Организовать функцию countBasketPrice, которая будет считать стоимость корзины

function countBasketPrice() {
    let basket = [
        {
            title: 'Product-1',
            price: 1250,
            count: 10
        },
        {
            title: 'Product-2',
            price: 360,
            count: 12
        },
        {
            title: 'Product-3',
            price: 470,
            count: 8
        },
    ];

    let sum = 0;
    let quantity = 0;
    let text = 'В корзине находятся следующие позиции: '; 

    for (var item of basket) {
        sum +=(item.price * item.count);
        quantity += item.count; 
        text += '(' + item.title + ')';
        }

    let q = basket.length;


    return 'Всего товаров в корзине:' + q + '. ' + text + '. ' + 'Общее количество выбранных позиций состовляет, шт.:'
    + quantity + '. ' + 'Стоимость всез товаров в корзине составляет, руб.:' + sum + '.';
}

console.log(countBasketPrice());