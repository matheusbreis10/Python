# -*- coding: utf-8 -*-

import pygame
import sys
import os
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,239,0)
lista =[]


class Player():
    def __init__(self):
        self.robo = pygame.draw.rect(screen,BLUE,[[90,50],[20,20]])
        self.nao_permitido_corrigido = []
        self.pos = 1
        self.var = '1'
        
    def draw(self, surface):
        pygame.draw.rect(screen,WHITE,[[-1,-1],[450,600]])
        pygame.draw.rect(screen, (0, 0, 128), self.robo)
        if pygame.draw.rect(screen,YELLOW,[[410,460],[60,50]]) == True:
            pygame.draw.rect(screen,YELLOW,[[410,460],[60,50]])
        else:
            pygame.draw.rect(screen,BLUE,[[410,460],[60,50]])
            
        #pygame.draw.rect(screen,WHITE,[[-1,-1],[450,600]])
        welcomeFont = pygame.font.Font(None, 25)
        welcomeMessage = welcomeFont.render("Movimentos:", True, YELLOW)
        welcomeMessage2 = welcomeFont.render("FIM", True, WHITE)
        up_arrow_red = pygame.image.load('images/up_arrow_red.png')
        left_arrow_red = pygame.image.load('images/left_arrow_red.png')
        down_arrow_green = pygame.image.load('images/down_arrow_green.png')
        right_arrow_green = pygame.image.load('images/right_arrow_green.png')
        
        screen.blit(up_arrow_red, (480,70))
        screen.blit(left_arrow_red, (480,140))
        screen.blit(down_arrow_green, (480,210))
        screen.blit(right_arrow_green, (480,280))
        screen.blit(welcomeMessage2, (425,475))
        screen.blit(welcomeMessage, (460, 30))
        
    def vencedor(self):
   
        if [self.robo[0],self.robo[1]] == [390,470]:
            lista.append('Vitoria')
            pygame.display.flip()
            pygame.draw.rect(screen,WHITE,[[-1,-1],[450,600]])
            pygame.draw.rect(screen, (0, 0, 128), self.robo)
            self.robo = pygame.draw.rect(screen,YELLOW,[[390,470],[20,20]])
            pygame.draw.rect(screen,YELLOW,[[410,460],[60,50]])
            welcomeFont = pygame.font.Font(None, 25)
            welcomeMessage2 = welcomeFont.render("FIM", True, BLACK)
            screen.blit(welcomeMessage2, (425,475))  
            #Player.play_again(self)
            
    def caminho(self):
        pygame.draw.line(screen, WHITE, [0, 0], [640, 0], 5)
        
        for i in range (1,5):
            for j in range (1,9):
                pygame.draw.circle(screen, GREEN, [100*i, 60*j], 5)
        
        pygame.draw.circle(screen, RED, [200, 120], 5)
        pygame.draw.circle(screen, RED, [300, 180], 5)
        pygame.draw.circle(screen, RED, [100, 240], 5)
        pygame.draw.circle(screen, RED, [300, 300], 5)
        pygame.draw.circle(screen, RED, [400, 360], 5)
        pygame.draw.circle(screen, RED, [400, 420], 5)
        pygame.draw.circle(screen, RED, [200, 420], 5)
        pygame.draw.circle(screen, RED, [200, 480], 5)
        self.nao_permitido_corrigido = [[190,110],[290,170],[90,230],[290,290],[390,350],\
                 [390,410],[190,470]]

    def movimento(self):
        key = pygame.key.get_pressed()
        Player.confere(self)
        if not key == False:
            if self.pos == 1:
                if event.type == pygame.KEYDOWN:
                    #   self.robo.move_ip(-100, 0)
                    if key[pygame.K_RIGHT]:
                       if not self.robo[0] > 300:
                           self.robo.move_ip(100, 0)
                    #if key[pygame.K_UP]:
                    #   self.robo.move_ip(0, -60)
                    if key[pygame.K_DOWN]:
                        if not self.robo[1] > 420:
                            self.robo.move_ip(0, 60)
        else:
            pass
                              
    
    def play_again(self):
        play_again = pygame.image.load('images/play.png').convert()
        screen.blit(play_again,(500,420))

        if pygame.mouse.get_pos() >= (500,420) and pygame.mouse.get_pos() <= (564,484):
            if event.type == pygame.MOUSEBUTTONDOWN:            
                restart_program()


        
    def game_over(self):
        game_Over = pygame.image.load('images/skull.png')
        screen.blit(game_Over,(500,460))
        #pygame.quit()
        #sys.exit()   
        
    def confere(self):
        for i in range(0,len(self.nao_permitido_corrigido)):
            if [self.robo[0],self.robo[1]] == self.nao_permitido_corrigido[i]:
                self.pos = 0
                #print('Movimento nao permitido. ')
                Player.game_over(self)
                
            else:
                self.pos = 1

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 600))
# carregando fonte
font = pygame.font.SysFont(None, 55)
pygame.display.set_caption('Robô')

# preenchendo o fundo com preto
screen.fill(BLACK)
player = Player()
pygame.display.flip()
while player.var == '1':
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if player.var == '1':
            player.draw(screen)
            if lista == []:
                player.vencedor()
            player.caminho()
            player.play_again()
            player.movimento()
            pygame.display.update()

        clock.tick(40)
        
