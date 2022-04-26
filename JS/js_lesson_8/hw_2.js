//a
if (!("a" in window)) {
    var a = 1;
    }
    alert(a);
//В данном примере браузер выведет undefined потому что по условию if строка должна быть неистинной, т.е. без значения, а она имеет числовое значение 1, значит условие не соблюдается, 
//а на этот случай условия вывода нет (undefined), что и выводится в alert.

//b
var b = function a(x) {
    x && a(--x);
    };
    alert(a);
//В данном примере браузер не выведет ничего, т.к. "а" - это имя функции и в теле функции не определено какое-либо действие.

//c
function a(x) {
    return x * 2;
    }
    var a;
    alert(a);
//В данном примере браузер не выведет ничего, т.к. переменная "a" объявлена без указания значения, а значит в "alert" выводится функция "а", 
//для которой значение переменной "x", указанной в функции, отсутствует.

//d
function b(x, y, a) {
    arguments[2] = 10;
    alert(a);
    }
    b(1, 2, 3);    
//В данном примере браузер выведет в "alert" значение третьего аргумента, которому присвоено значение 10 в теле функции.

//e
function a() {
    alert(this);
    }
    a.call(null);
//Слово "this" обозначает объект, который запускает данную функцию. здесь объект отсутствует, значит "this" ничего не обозначает. 
//Браузер понимает, что должен бытьобъект, но не видит какой. 
//В "flert" будет указано, что это объект без названия.