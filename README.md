# 1C_project. Задача на алгоритмы.

## Задача.

Предыстория: так как моё направление учёбы и дальнейшей работы связанно с машинным обучением, я не выбирал задания на сис. программирование, так как не обладаю достаточными навыками (у меня просто другое направление), именно поэтому я выбрал задачу на алгоритмы.

Задача показалась сложной (не знаю, хорошо это или плохо). Получилось что-то реализовать, эта реализация даже проходит простые тесты, которые приведены ниже. Наверно, если бы не нагрузка по другим предметам, получилось бы лучше. В любом случае — потренировался прогать на питоне! Надеюсь, что решение не совсем ужасно, потому что есть **большое желание попасть к вам на кафедру**, надеюсь одна не идеально решенная задача всё не испортит.

**Note.** Нормально протестировать решение (используя unittest, например) тоже не успел, к сожалению. Понимаю, как должно выглядеть идеальное решение: оно не должно базироваться на двух-трёх частных тестах.

### Решение задачи (описание, что происходит).

#### Class Card — класс для игральной карты.

`from_str()` — статический метод, который создаёт объект класса по представлению карты строкой. (ну то есть, "6D" мы присваиваем карту со значением 6, например)

`goes_on(other)` — проверяет, можно ли карту положить на другую (то есть сравнивает корректность по их значениям)

Далее я переопределил разные магические методы, по названиям которых понятно, зачем они нужны. Отдельно отмечу, что магический метод `__hash__` я переопределил, чтобы была возможность складывать карты в `set()` (потому что `set()` — это хеш-таблица, поэтому объекты в нём должны быть хешируемыми)

#### Class Board — класс для доски (доска — это набор из 72 игральных карт, то есть все 8 кучек по 9 карт я называю просто доской)





