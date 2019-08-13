import sys
import pygame

pygame.init()  # initiates pygame function

print("Tic Tac Toe")
size = width, height = 320, 240
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
cyan = 0, 255, 255

screen = pygame.display.set_mode(size)  # resolution of the game
pygame.display.set_caption("Tic Tac Toe")  # title of window
clock = pygame.time.Clock()  # frames per second (game clock)
turn = True
# block = pygame.image.load('block.png')  # load images in


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def players():
    player1 = "X"
    player2 = "O"
    if turn is True:
        return player1
    elif turn is False:
        return player2


class Winner:
    def __init__(self, border, player):
        self.border = border
        self.player = player
        self.data = border, player


def scoreboard():
    score1 = 0
    score2 = 0
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Player 1: " + str(score1), smallText)
    textRect.center = (53, 12)
    screen.blit(textSurf, textRect)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Player 2: " + str(score2), smallText)
    textRect.center = (53, 35)
    screen.blit(textSurf, textRect)


def background():
    pygame.draw.rect(screen, black, pygame.Rect(0, 50, 106, 63))  # upper left square
    pygame.draw.rect(screen, black, pygame.Rect(0, 114, 106, 63))  # middle left square
    pygame.draw.rect(screen, black, pygame.Rect(0, 178, 106, 63))  # lower left square

    pygame.draw.rect(screen, black, pygame.Rect(107, 50, 106, 63))  # upper center square
    pygame.draw.rect(screen, black, pygame.Rect(107, 114, 106, 63))  # middle center square
    pygame.draw.rect(screen, black, pygame.Rect(107, 178, 106, 63))  # lower center square

    pygame.draw.rect(screen, black, pygame.Rect(214, 50, 106, 63))  # upper right square
    pygame.draw.rect(screen, black, pygame.Rect(214, 114, 106, 63))  # middle right square
    pygame.draw.rect(screen, black, pygame.Rect(214, 178, 106, 63))  # lower right square


border_list = []


def set_player(border):
    if border not in border_list:
        border_list.append(border)

        pygame.draw.rect(screen, white, border)
        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = text_objects(players(), smallText)
        textRect.center = ((border[0] + (106 / 2)), (border[1] + (63 / 2)))
        screen.blit(textSurf, textRect)
        winner = Winner(border, players())
        check_winner(winner.data)


# horizontal rows
top_row = []
square_top_row = []
middle_row = []
square_middle_row = []
bottom_row = []
square_bottom_row = []
# veritcal rows
first_column = []
square_first_column = []
sec_column = []
square_sec_column = []
third_column = []
square_third_column = []
# diagonals
forward_slash = []  # /
square_forward_slash = []  # /
back_slash = []  # \
square_back_slash = []  # \


def winner(pos, area):
    if "O" not in pos:
        print("WINNER: PLAYER 1!")
        game_finished(area)
    elif "X" not in pos:
        print("WINNER: PLAYER 2!")
        game_finished(area)
    if len(border_list) == 9 and "X" in pos and "O" in pos:
        print("The game is a tie!")


def check_winner(data):
    # horizontal rows
    if data[0][1] == 50:
        top_row.append(data[1])
        square_top_row.append(data[0])
        if len(top_row) == 3:
            winner(top_row, square_top_row)
    elif data[0][1] == 114:
        middle_row.append(data[1])
        square_middle_row.append(data[0])
        if len(middle_row) == 3:
            winner(middle_row, square_middle_row)
    elif data[0][1] == 178:
        bottom_row.append(data[1])
        square_bottom_row.append(data[0])
        if len(bottom_row) == 3:
            winner(bottom_row, square_bottom_row)
    # vertical rows
    if data[0][0] == 0:
        first_column.append(data[1])
        square_first_column.append(data[0])
        if len(first_column) == 3:
            winner(first_column, square_first_column)
    elif data[0][0] == 107:
        sec_column.append(data[1])
        square_sec_column.append(data[0])
        if len(sec_column) == 3:
            winner(sec_column, square_sec_column)
    elif data[0][0] == 214:
        third_column.append(data[1])
        square_third_column.append(data[0])
        if len(third_column) == 3:
            winner(third_column, square_third_column)
    # forward slash diagonal
    if data[0][0] == 0 and data[0][1] == 178 or data[0][0] == 107 and data[0][1] == 114 or data[0][0] == 214 \
            and data[0][1] == 50:
        forward_slash.append(data[1])
        square_forward_slash.append(data[0])
        if len(forward_slash) == 3:
            winner(forward_slash, square_forward_slash)
    # back slash diagonal
    if data[0][0] == 0 and data[0][1] == 50 or data[0][0] == 107 and data[0][1] == 114 or data[0][0] == 214 \
            and data[0][1] == 178:
        back_slash.append(data[1])
        square_back_slash.append(data[0])
        if len(back_slash) == 3:
            winner(back_slash, square_back_slash)


def game_finished(area):
    print("The game is over!")
    for i in range(0, 3):
        pygame.draw.rect(screen, cyan, area[i], 3)


def clicked():
    if 0 + 106 > mouse[0] > 0 and 50 + 63 > mouse[1] > 50:
        square1 = pygame.Rect(0, 50, 106, 63)
        set_player(square1)
    elif 0 + 106 > mouse[0] > 0 and 114 + 63 > mouse[1] > 114:
        square2 = pygame.Rect(0, 114, 106, 63)
        set_player(square2)
    elif 0 + 106 > mouse[0] > 0 and 178 + 63 > mouse[1] > 178:
        square3 = pygame.Rect(0, 178, 106, 63)
        set_player(square3)
    elif 107 + 106 > mouse[0] > 107 and 50 + 63 > mouse[1] > 50:
        square4 = pygame.Rect(107, 50, 106, 63)
        set_player(square4)
    elif 107 + 106 > mouse[0] > 107 and 114 + 63 > mouse[1] > 114:
        square5 = pygame.Rect(107, 114, 106, 63)
        set_player(square5)
    elif 107 + 106 > mouse[0] > 107 and 178 + 63 > mouse[1] > 178:
        square6 = pygame.Rect(107, 178, 106, 63)
        set_player(square6)
    elif 214 + 106 > mouse[0] > 214 and 50 + 63 > mouse[1] > 50:
        square7 = pygame.Rect(214, 50, 106, 63)
        set_player(square7)
    elif 214 + 106 > mouse[0] > 214 and 114 + 63 > mouse[1] > 114:
        square8 = pygame.Rect(214, 114, 106, 63)
        set_player(square8)
    elif 214 + 106 > mouse[0] > 214 and 178 + 63 > mouse[1] > 178:
        square9 = pygame.Rect(214, 178, 106, 63)
        set_player(square9)


screen.fill(white)
pygame.draw.rect(screen, red, pygame.Rect(0, 0, 320, 50))  # x, y, width, height
background()
scoreboard()

while 1:
    mouse = pygame.mouse.get_pos()  # gets mouse position
    click = pygame.mouse.get_pressed()  # gets mouse clicks

    for event in pygame.event.get():  # gets any event that happens (mouse movement, clicks, key presses)
        if event.type == pygame.QUIT:  # exited the window quits program
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse[1] > 50:
            clicked()
            if turn is True:
                turn = False
            else:
                turn = True

    pygame.display.update()  # or pygame.display.flip()
    clock.tick(30)  # frames per second
