//Мне кажется, что есть вариант использования замыкания при определении координат для обеспечения перемещения змейки на другую сторону при достижении границ поля игры.

function coordXY (newUnit) {

    return function (arg1, arg2, arg3, arg4) {

      if (new_unit == newUnit && direction == arg1) {
       new_unit = document.getElementsByClassName('cell-' + (coord_y) + '-' + (FIELD_SIZE_X - 1))[0];

      } else if (new_unit == newUnit && direction == arg2) {
       new_unit = document.getElementsByClassName('cell-' + (coord_y) + '-' + (0))[0];

      } else if (new_unit == newUnit && direction == arg3) {
       new_unit = document.getElementsByClassName('cell-' + (FIELD_SIZE_Y - 1) + '-' + (coord_x))[0];

      } else if (new_unit == newUnit && direction == arg4) {
       new_unit = document.getElementsByClassName('cell-' + (0) + '-' + (coord_x))[0];
       }
    }
}
var s = coordXY(undefined); //Создаем переменную "s" и присваиваем ей результат вывода функции "coordXY(newUnit)" 
//со значением "newUnit === undefined", в качестве первого условия, необходимого для создания телепортации.
s('x-', 'x+', 'y+', 'y-'); //После того, как переменная "s" "стала" функцией, присваиваем ей входящие значения для вложенной функции, 
//соответствующие направлениям изменения координат "s('x-', 'x+', 'y+', 'y-');".