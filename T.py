import pygame
import sys
import time

class TicTacToeGame:
    def __init__(self):
        pygame.init()
        self.fps = 30
        self.CLOCK = pygame.time.Clock()
        self.width = 400
        self.height = 400
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.winner = None
        self.board = [[None] * 3, [None] * 3, [None] * 3]
        self.XO = 'x'

        self.win = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.x_image = pygame.image.load("X.png")
        self.o_image = pygame.image.load("o.png")

        self.x_image = pygame.transform.scale(self.x_image, (80, 80))
        self.o_image = pygame.transform.scale(self.o_image, (80, 80))

        pygame.display.set_caption('TicTacToe')

    def display_winner(self, winner):
        self.win.fill(self.white)
        font = pygame.font.Font(None, 36)
        if winner == 'x':
            text = font.render("Player X wins!", True, self.black)
        elif winner == 'o':
            text = font.render("Player O wins!", True, self.black)
        else:
            text = font.render("It's a tie!", True, self.black)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.win.blit(text, text_rect)
        self.draw_reset_button()
        pygame.display.update()

    def draw(self):
        self.win.fill(self.white)
        pygame.draw.line(self.win, self.black, (self.width/3, 0), (self.width/3, self.height), 7)
        pygame.draw.line(self.win, self.black, (self.width/3 * 2, 0), (self.width/3 * 2, self.height), 7)
        pygame.draw.line(self.win, self.black, (0, self.height/3), (self.width, self.height/3), 7)
        pygame.draw.line(self.win, self.black, (0, self.height/3 * 2), (self.width, self.height/3 * 2), 7)

    def is_win(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                self.winner = self.board[row][0]
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                self.winner = self.board[0][col]
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.winner = self.board[0][2]
            return True
        return False

    def drawXO(self, row, col):
        if row == 1:
            posx = 30
        if row == 2:
            posx = self.width / 3 + 30
        if row == 3:
            posx = self.width / 3 * 2 + 30
        if col == 1:
            posy = 30
        if col == 2:
            posy = self.height / 3 + 30
        if col == 3:
            posy = self.height / 3 * 2 + 30

        self.board[row-1][col-1] = self.XO

        if self.XO == 'x':
            self.win.blit(self.x_image, (posy, posx))
            self.XO = 'o'
        else:
            self.win.blit(self.o_image, (posy, posx))
            self.XO = 'x'

        pygame.display.update()

    def userClick(self):
        x, y = pygame.mouse.get_pos()

        if x < self.width/3:
            col = 1
        elif x < self.width/3 * 2:
            col = 2
        elif x < self.width:
            col = 3
        else:
            col = None

        if y < self.height/3:
            row = 1
        elif y < self.height/3 * 2:
            row = 2
        elif y < self.height:
            row = 3
        else:
            row = None

        if row and col and self.board[row-1][col-1] is None:
            self.drawXO(row, col)
            if self.is_win():
                self.display_winner(self.winner)

        self.check_reset_button_click((x, y))  # Check for reset button click

    def reset(self):
        time.sleep(1)
        self.XO = 'x'
        self.draw()
        self.winner = None
        self.board = [[None] * 3, [None] * 3, [None] * 3]

    def draw_reset_button(self):
        reset_button_rect = pygame.Rect(self.width // 2 - 50, self.height // 2 + 50, 100, 40)
        pygame.draw.rect(self.win, self.black, reset_button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render("Reset", True, self.white)
        text_rect = text.get_rect(center=reset_button_rect.center)
        self.win.blit(text, text_rect)

    def check_reset_button_click(self, pos):
        reset_button_rect = pygame.Rect(self.width // 2 - 50, self.height // 2 + 50, 100, 40)
        if reset_button_rect.collidepoint(pos):
            self.reset()

    def run_game(self):
        self.draw()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.userClick()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.winner is not None:
                        self.reset()

            pygame.display.update()
            self.CLOCK.tick(self.fps)

game = TicTacToeGame()
game.run_game()
