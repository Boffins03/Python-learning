import random
import turtle

win_length = 500
win_height = 500
turtles = 8

turtle.screensize(win_length, win_height)


class Racer:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randint(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def setup_file(name, colors):
    with open(name, 'w') as file:
        for color in colors:
            file.write(f"{color} 0\n")


def start_game():
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
    t_list = []
    start = -(win_length / 2) + 20
    for i, color in enumerate(colors[:turtles]):
        new_pos_x = start + i * (win_length) // turtles
        t_list.append(Racer(color, (new_pos_x, -230)))
        t_list[i].turt.showturtle()

    while any(t.pos[1] < 230 for t in t_list):
        for t in t_list:
            t.move()

    winners = [t.color for t in t_list if t.pos[1] >= 230]
    print('The winner is: ', ', '.join(winners))

    with open('scores.txt', 'r+') as file:
        old_scores = [line.strip().split() for line in file]
        file.seek(0)
        for entry in old_scores:
            for winner in winners:
                if entry[0] == winner:
                    entry[1] = str(int(entry[1]) + 1)
            file.write(' '.join(entry) + '\n')
        file.truncate()


def play_again():
    while True:
        choice = input('Would you like to play again (yes/no): ').lower()
        if choice == 'yes':
            start_game()
        elif choice == 'no':
            print('Thank you for playing!')
            break
        else:
            print('Invalid input. Please enter yes or no.')


def main():
    start = input('Would you like to play: ').lower()
    if start == 'yes':
        start_game()
        play_again()
    else:
        print('Maybe next time!')


if __name__ == "__main__":
    main()
