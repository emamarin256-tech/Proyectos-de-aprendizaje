import os
import pygame
from Control.control_nave import Ship

class controldellaser:
    def __init__(self, game):
        self.game = game
        imagen_original = pygame.image.load(os.path.join('Aliens-Attack/imagenes', 'laser.png'))
        nuevo_tamaño = (50, 50)
        self.laser_imagen = pygame.transform.scale(imagen_original, nuevo_tamaño)
        self.lista_laser = []
        self.puede_disparar=True
        self.tiempo_de_disparo=None
        self.cadencia=500
    
        
    def evento_disparo(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and self.puede_disparar:
            self.shoot()

    def shoot(self):
        nacimiento_laser=self.laser_imagen.get_rect(midbottom=self.game.conrol_nave.rect.midtop)
        self.lista_laser.append(nacimiento_laser)
        self.puede_disparar = False
        self.tiempo_de_disparo = pygame.time.get_ticks()
        self.game.sonido_laser.play()
 
    def update(self):
        for laser_individual in self.lista_laser[:]:
            laser_individual.y -= 300*self.game.dt 
            if laser_individual.bottom < 0:
                self.lista_laser.remove(laser_individual)
        self.actualizar_tiempo()
    
    def actualizar_tiempo(self):
        if not self.puede_disparar:
            current_time = pygame.time.get_ticks()
            if current_time - self.tiempo_de_disparo > self.cadencia:
                self.puede_disparar=True

    def imagen(self, surface):
        for rect in self.lista_laser:
            surface.blit(self.laser_imagen,rect)