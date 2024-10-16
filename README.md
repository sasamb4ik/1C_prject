# 1C_project. Задача на алгоритмы.

## Задача.

Предыстория: так как моё направление учёбы и дальнейшей работы связанно с машинным обучением, я не выбирал задания на сис. программирование, так как не обладаю достаточными навыками в этом направлении, именно поэтому я выбрал задачу на алгоритмы и решил писать её на Python, опять же потому что это мой самый рабочий язык в силу моего направления.

Задача показалась сложной (не знаю, хорошо это или плохо). Получилось что-то реализовать, эта реализация даже проходит простые тесты, которые приведены ниже. Наверно, если бы не нагрузка по другим предметам, получилось бы лучше. В любом случае — потренировался прогать на питоне! Надеюсь, что решение не совсем ужасно, потому что есть **большое желание попасть к вам на кафедру**, надеюсь одна не идеально решенная задача всё не испортит.

**Note.** Нормально протестировать решение (используя unittest, например) тоже не успел, к сожалению. Понимаю, как должно выглядеть идеальное решение: оно не должно базироваться на двух-трёх частных тестах.

### Решение задачи (описание, что происходит).

#### Формат ввода

В решении я кодирую значения карт следующим образом: цифры 6-9 остаются без изменений, 10 кодируется как X, валет: V, дама: D, король: K, туз: A.

Масти кодируются как: C - clubs, S - spades, H - hearts, D - diamonds. То есть, например "DD" означет Дама Diamonds, то есть дама руби и так далее.

#### Class Card — класс для игральной карты.

`from_str()` — статический метод, который создаёт объект класса по представлению карты строкой. (ну то есть, "6D" мы присваиваем карту со значением 6, например)

`goes_on(other)` — проверяет, можно ли карту положить на другую (то есть сравнивает корректность по их значениям)

Далее я переопределил разные магические методы, по названиям которых понятно, зачем они нужны. Отдельно отмечу, что магический метод `__hash__` я переопределил, чтобы была возможность складывать карты в `set()` (потому что `set()` — это хеш-таблица, поэтому объекты в нём должны быть хешируемыми)

#### Class Board — класс для доски (доска — это набор из 72 игральных карт, то есть все 8 кучек по 9 карт я называю просто доской)

`is_complete()` — проверяет, что есть правильно упорядоченная кучка

`legal_moves()` — перемещает карты. Есть два случая: либо убрать верхнюю карту из текущей кучки и переместить в другую, либо убрать сразу несколько карт (если они в правильном порядке). После изменений создаёт новый `Board()`

`clone()` — нужна для `legal_moves()`, клонирует текущую "доску".

Остальные функции понятны из названия.

### Алгоритм решения

В решении я использую аналогичный BFS подход, почему именно BFS: в задаче нам нужно рассмотреть все возможные варианты, их можно представить как графовую структуру, которую нужно обойти (и при обходе нам нужны правильные кучки). Интуитивно BFS здесь логичнее, чем DFS, так как BFS позволит раньше найти ответ в ближних кучках и не нужно будет идти вглубь, логичнее обходить кучки, которые ближе. 

Эта логика реализована в функции `solve()`

### Assert'ы

Также я добавил несколько ассёртов рейзов в реализацию, например я отлавливаю некорректное количество поданных кард на вход, неверный формат ввода. Также есть проверка на то, не потрят ли вышеописанные функции доску (добавил проверку, что её размер должен быть константым и не меняеться - 72)

### Асимптотика

Решение зависит от общего количества комбинаций, поэтому эффективное решение, гарантированно работающее быстро и правильно у меня найти не получилось. Асимптотику можно оценить как $ O(n^d) $, где $n$ это количество упорядочиваний кучки, $d$ это глубина дерева. Понятно, что дождаться этого нормально невозможно. **Решение** - можно получить приближённый ответ, сделав отсечку по количеству итераций алгоритма (что я и сделал), если мое решение не находит ответ за `number_of_iter = 10000`, то я возвращаю что "Решение не найдено, но возможно оно есть".

### Тесты

Сделаем ввод, где сразу есть правильно упорядоченная кучка (см. первую кучку, она сразу упорядочена):

![Screenshot from 2024-10-13 23-20-56](https://github.com/user-attachments/assets/8ebab2e2-3067-45f0-8b8d-fc922450de31)

Ещё один простой тест:

![Screenshot from 2024-10-13 23-27-35](https://github.com/user-attachments/assets/49701740-84fc-4ed0-8a84-718fa9f67053)

Решение: удалить из первой кучки `VD, XD, 9D, 8D, 7D, 6D, 6H` (7 операций), далее положить из второй кучки в первую `DS` (1 операция), далее вернуть 6 элементов из первой кучки обратно (6 операций).





