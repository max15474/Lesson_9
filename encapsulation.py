import random
class Dice_inc:
    def __init__(self, N):
        self.throw_num = N
        self.current_throw = 0

    def set_hidden_numbers(self):
        self.__hidden_num_1 = random.randint(1, 6)
        self.__hidden_num_2 = random.randint(1, 6)

    def change_dices(self):
        self.__hidden_num_1 = random.randint(1, 6)
        self.__hidden_num_2 = random.randint(1, 6)

    def set_dice1(self, dice):
        self.__hidden_num_1 = dice

    def get_dice1(self):
        return self.__hidden_num_1
