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


class Tiles:
    def __init__(self, area, color, player, state):
        self.area = area  # area of rectange position [x, y, width, height]
        self.color = color  # color of the tile (black = inactive) (white = active)
        self.player = player  # which player is there? X or O
        self.state = state  # true or false is there a player there?


def scoreboard(score1, score2):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Player 1: " + str(score1), smallText)
    textRect.center = (53, 12)
    pygame.draw.rect(screen, red, pygame.Rect(0, 0, 320, 50))
    screen.blit(textSurf, textRect)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Player 2: " + str(score2), smallText)
    textRect.center = (53, 35)
    screen.blit(textSurf, textRect)


def background():
    # pygame.draw.rect(screen, black, pygame.Rect(0, 50, 106, 63))  # upper left square
    pygame.draw.rect(screen, topRowLeftTile.color, topRowLeftTile.area)  # upper left square
    pygame.draw.rect(screen, midRowLeftTile.color, midRowLeftTile.area)  # middle left square
    pygame.draw.rect(screen, botRowLeftTile.color, botRowLeftTile.area)  # lower left square

    pygame.draw.rect(screen, topRowMidTile.color, topRowMidTile.area)  # upper center square
    pygame.draw.rect(screen, midRowMidTile.color, midRowMidTile.area)  # middle center square
    pygame.draw.rect(screen, botRowMidTile.color, botRowMidTile.area)  # lower center square

    pygame.draw.rect(screen, topRowRightTile.color, topRowRightTile.area)  # upper right square
    pygame.draw.rect(screen, midRowRightTile.color, midRowRightTile.area)  # middle right square
    pygame.draw.rect(screen, botRowRightTile.color, botRowRightTile.area)  # lower right square


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


# data storage for winner checking
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
        scoreboard(1, 0)
        game_finished(area)
    elif "X" not in pos:
        print("WINNER: PLAYER 2!")
        game_finished(area)
    elif len(border_list) == 9 and "X" in pos and "O" in pos:
        print("The game is a tie!")


def game_finished(area):
    print("The game is over!")
    for i in range(len(area)):
        pygame.draw.rect(screen, cyan, area[i], 3)


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


topRowLeftTile = Tiles((0, 50, 106, 63), black, "?", False)
topRowMidTile = Tiles((107, 50, 106, 63), black, "?", False)
topRowRightTile = Tiles((214, 50, 106, 63), black, "?", False)

midRowLeftTile = Tiles((0, 114, 106, 63), black, "?", False)
midRowMidTile = Tiles((107, 114, 106, 63), black, "?", False)
midRowRightTile = Tiles((214, 114, 106, 63), black, "?", False)

botRowLeftTile = Tiles((0, 178, 106, 63), black, "?", False)
botRowMidTile = Tiles((107, 178, 106, 63), black, "?", False)
botRowRightTile = Tiles((214, 178, 106, 63), black, "?", False)


def clicked():
    if 0 + 106 > mouse[0] > 0 and 50 + 63 > mouse[1] > 50:  # inside the area of square1 - mouse = (x, y)
        set_player(topRowLeftTile.area)
    elif 0 + 106 > mouse[0] > 0 and 114 + 63 > mouse[1] > 114:
        set_player(midRowLeftTile.area)
    elif 0 + 106 > mouse[0] > 0 and 178 + 63 > mouse[1] > 178:
        set_player(botRowLeftTile.area)
    elif 107 + 106 > mouse[0] > 107 and 50 + 63 > mouse[1] > 50:
        set_player(topRowMidTile.area)
    elif 107 + 106 > mouse[0] > 107 and 114 + 63 > mouse[1] > 114:
        set_player(midRowMidTile.area)
    elif 107 + 106 > mouse[0] > 107 and 178 + 63 > mouse[1] > 178:
        set_player(botRowMidTile.area)
    elif 214 + 106 > mouse[0] > 214 and 50 + 63 > mouse[1] > 50:
        set_player(topRowRightTile.area)
    elif 214 + 106 > mouse[0] > 214 and 114 + 63 > mouse[1] > 114:
        set_player(midRowRightTile.area)
    elif 214 + 106 > mouse[0] > 214 and 178 + 63 > mouse[1] > 178:
        set_player(botRowRightTile.area)


screen.fill(white)
pygame.draw.rect(screen, red, pygame.Rect(0, 0, 320, 50))  # x, y, width, height - scoreboard
background()
scoreboard(0, 0)

while 1:
    mouse = pygame.mouse.get_pos()  # gets mouse position
    click = pygame.mouse.get_pressed()  # gets mouse clicks

    for event in pygame.event.get():  # gets any event that happens (mouse movement, clicks, key presses)
        if event.type == pygame.QUIT:  # exited the window quits program
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse[1] > 50:  # add condition for areas that have been clicked
            clicked()  # click the same area twice and the next area can be the same player
            if turn is True:
                turn = False
            else:
                turn = True

    pygame.display.update()  # or pygame.display.flip()
    clock.tick(30)  # frames per second
