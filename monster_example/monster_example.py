import random


class Monster:
    def __init__(self, n_rows, n_cols, max_speed):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.my_row = random.randrange(self.n_rows)
        self.my_col = random.randrange(self.n_cols)
        self.my_speed_x = random.randrange(-max_speed, max_speed + 1)
        self.my_speed_y = random.randrange(-max_speed, max_speed + 1)

    def move(self):
        self.my_row = (self.my_row + self.my_speed_x) % self.n_rows
        self.my_col = (self.my_col + self.my_speed_x) % self.n_cols


if __name__=='__main__':
    N_MONSTERS = 20
    N_ROWS = 100
    N_COLS = 200
    MAX_SPEED = 4
    monster_list = []
    for i in range(N_MONSTERS):
        the_monster = Monster(N_ROWS, N_COLS, MAX_SPEED)
        monster_list.append(the_monster)

    for the_monster in monster_list:
        the_monster.move()
