// Задание №2 Продолжить работу с интернет-магазином:
//a. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими
//объектами можно заменить их элементы?
//b. Реализуйте такие объекты.
//c. Перенести функционал подсчета корзины на объектно-ориентированную базу.

class product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }
}

class basket extends product {
    constructor(name, price, count, sum) {
        super(name, price);
        this.count = count;
        this.sum = sum;
    }
    sumBasket() {
        this.sum = this.count * this.price;
        console.log('Сумма корзины ' + this.sum);
    }
}

productsInBasket = [
    new basket('Apple', 50, 13),
    new basket('Orange', 35, 20),
    new basket('Banan', 72, 10)
];

productsInBasket[1].sumBasket();