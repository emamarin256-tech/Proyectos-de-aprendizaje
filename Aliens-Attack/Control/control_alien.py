import os
import pygame
import sys
from random import randint, uniform
class control_alien:
    def __init__(self, game):
        self.game = game
        imagen_original =pygame.image.load(os.path.join('Aliens-Attack/imagenes','alien.png'))
        nuevo_tamaño = (60, 60)
        self.mov_alien = pygame.transform.scale(imagen_original, nuevo_tamaño)
        self.mask = pygame.mask.from_surface(self.mov_alien)
        self.lista_alien = []
        self.tiempo__alien = pygame.event.custom_type()
        pygame.time.set_timer(self.tiempo__alien,200)
        
    def evento_alien(self, event):
        if event.type == self.tiempo__alien:
            self.movimiento_alien()
    
    def movimiento_alien(self):
        x_pos = randint(-100, self.game.WINDOW_WIDTH + 100)
        Y_pos = randint(-100,-50)
        
        alien_pos = self.mov_alien.get_rect(center=(x_pos,Y_pos))
        direccion = pygame.math.Vector2(uniform(-0.5,0.5), 1)
        self.lista_alien.append((alien_pos,direccion))
    
    def update(self):
        for alien_tuple in self.lista_alien[:]:

            direccion = alien_tuple[1]

            alien_pos = alien_tuple[0]

            alien_pos.center +=direccion*300*self.game.dt

            if alien_pos.top > self.game.WINDOW_HEIGHT:
                self.lista_alien.remove(alien_tuple)
        
    def imagen(self,surface):
        for alien_tuple in self.lista_alien:
            surface.blit(self.mov_alien,alien_tuple[0] )
    
