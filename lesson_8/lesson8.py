# # Алгоритм **игры** крестики-нолики
# 1. Рисуется **поле** [создается пустая матрица]
# 2. Пока **игра** не закончена:
#    2. **Игрок** выбирает куда поставить **символ**
#    3. Проверить занята ли **клетка** \ валидный ли **ход**
#    3. Рисуется обновленное **поле**
#    4. Проверить победное **условия** \ окончания **игры**
#    5. Ход переходить другому **игроку**
# 6. Пишем кто победил
#
class Game:
    def __init__(self, field_size=3):
        self.field = Field(field_size)
        self.player_1 = Player('X')
        self.player_2 = Player('O')
        self.actual_player = self.player_1

    def start(self):
        pass

    def is_running(self):
        pass

    def switch_turn(self):
        pass

    def check_winning_condition(self):
        pass


# композиция # агрегация
class Field:
    def __init__(self):
        pass

    # def _check_if_cell_is_empty(self, coordinate):
    #     pass

    def set_symbol(self, symbol, coordinate):
        pass

    def print(self):
        pass

    # class Cell:
    #     pass

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_turn(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.start()
