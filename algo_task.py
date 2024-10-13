from collections import deque

class Card:
    '''
    В поле cards_names у нас кодировка кард. Цифры - очевидно
    Десятку кодируем Х
    Вальта кодируем V
    Даму кодируем Q
    Короля кодируем K
    Туза кодируем A
    '''
    cards_names = {
        "6": 6, "7": 7, "8": 8, "9": 9, "X": 10,
        "V": 11, "D": 12, "K": 13, "A": 14
    }

    convert_cards = {v: k for k, v in cards_names.items()}

    def __init__(self, number=None):
        if number:
            self.number = number

    @staticmethod
    def from_str(text):
        return Card(Card.cards_names[text[0]])

    def goes_on(self, other):
        return self.number + 1 == other.number

    def __str__(self):
        return Card.convert_cards[self.number]

    def __eq__(self, other):
        return isinstance(other, Card) and self.number == other.number

    def __lt__(self, other):
        return isinstance(other, Card) and self.number < other.number

    def __hash__(self):
        return hash(str(self))

class Board:
    def __init__(self, deck_argument):
        self.move_num = 0
        self.pile_illegal = [False] * 8
        assert len(deck_argument) == 72, (f"Ошибка! Длина"
                                          f" строки равна{len(deck_argument)}; "
                                          f"Но должна быть 72")
        self.piles = [deck_argument[i:i + 9] for i in range(0, 72, 9)]

    def __str__(self):
        piles_mod = self.piles
        largest_size = max(map(len, piles_mod)) + 1
        for stack, illegal in zip(piles_mod, self.pile_illegal):
            stack.extend([' '] * (largest_size - len(stack)))
            if illegal:
                stack.append('!')

        return '\n'.join([' '.join(map(str, r)) for r in zip(*piles_mod)])

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.piles == other.piles

    def __lt__(self, other):
        return self.piles < other.piles

    def __hash__(self):
        return hash(tuple(tuple(pile) for pile in self.piles))

    def is_complete(self):
        '''
        Тут и происходит проверка, если в куче есть правильный порядок
        от A (Ace) до 6 (шестерки)
        '''
        for pile in self.piles:
            if len(pile) == 9 and all(card.number == 14 - i for i, card in enumerate(pile)):
                return True
        return False

    def legal_moves(self):
        for idx, pile in enumerate(self.piles):
            if not pile:
                continue

            top_card = pile[-1]

            for dst_idx in range(len(self.piles)):
                # проверка, что не пойдем в ту же кучку карт
                if dst_idx == idx or self.pile_illegal[dst_idx]:
                    continue

                # если у верхней карты в другой куче меньше значение, то идем
                # туда
                if not self.piles[dst_idx] or top_card.goes_on(self.piles[dst_idx][-1]):
                    new_b = self.clone()
                    # двигаем самую верхнюю карту
                    new_b.piles[dst_idx].append(new_b.piles[idx].pop())
                    new_b.move_num += 1

                    if new_b.is_complete():
                        new_b.remove_complete_set(dst_idx)
                    yield new_b

            for idy in range(len(pile)):
                if pile[idy].number == top_card.number:
                    continue

                for dst_idx in range(len(self.piles)):
                    if dst_idx == idx or self.pile_illegal[dst_idx]:
                        continue

                    if not self.piles[dst_idx] or pile[idy].goes_on(self.piles[dst_idx][-1]):
                        new_b = self.clone()
                        new_b.piles[dst_idx].extend(new_b.piles[idx][idy:])
                        new_b.piles[idx] = new_b.piles[idx][:idy]
                        new_b.move_num += 1

                        if new_b.is_complete():
                            new_b.remove_complete_set(dst_idx)
                        yield new_b

    def clone(self):
        '''
        Создание доски
        '''
        new_board = Board(self.get_flat_deck())
        new_board.piles = [list(pile) for pile in self.piles]
        new_board.pile_illegal = self.pile_illegal.copy()
        new_board.move_num = self.move_num
        return new_board

    def get_flat_deck(self):
        return [card for pile in self.piles for card in pile]

    def remove_complete_set(self, pile_index):
        '''
        Удаляет из кучки карт полный набор (от Туза до шестерки), если он был найден
        '''
        if len(self.piles[pile_index]) == 9 and all(card.number == 14 - i for i, card in enumerate(self.piles[pile_index])):
            self.piles[pile_index] = []
            self.pile_illegal[pile_index] = False

    def score(self):
        """
        Считаем кол-во шагов
        """
        score = 0
        for pile in self.piles:
            if len(pile) == 9:
                score += 1
            score += len(pile)
        return score


def solve(board):

    seen = set()
    seen.add(board)
    queue = deque([board])
    finished = None

    move_limit = 10000

    while queue and (move_limit > 0):
        curr_b = queue.popleft()

        if curr_b.is_complete():
            finished = curr_b
            break

        for next_b in curr_b.legal_moves():
            if next_b not in seen:
                seen.add(next_b)
                queue.append(next_b)

        move_limit -= 1

    if finished:
        print("Решение существует!")
        print(f"Понадобилось сделать шагов: {finished.move_num}")
    else:
        print("Решение не найдено. Возможно, нужно подольше подождать")


if __name__ == "__main__":
    deck = []

    for pile_num in range(1, 9):
        while True:
            try:
                cards_input = input(
                    f"Введите ровно 9 кард для кучки номер {pile_num} ("
                    f"6D 7D 8D "
                    f"9D): "
                )
                cards = cards_input.strip().split()

                if len(cards) != 9:
                    raise ValueError("Я же сказал, РОВНО 9 карт!")

                pile_cards = [Card.from_str(card) for card in cards]
                deck.extend(pile_cards)
                break
            except Exception as e:
                print(f"Неверный ввод: {e}")

    solve(Board(deck))
