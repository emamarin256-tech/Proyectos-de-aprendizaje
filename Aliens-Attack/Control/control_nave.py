import pygame,sys,os


class Ship:

    def __init__(self, game):

        self.game = game
        imagen_original = pygame.image.load(os.path.join('Aliens-Attack/imagenes','nave.png'))
        nuevo_tamaño = (90, 90)
        self.imagen_nave = pygame.transform.scale(imagen_original, nuevo_tamaño)
        self.rect=self.imagen_nave.get_rect(center=((game.WINDOW_WIDTH/2 , game.WINDOW_HEIGHT/2)))
        self.mask = pygame.mask.from_surface(self.imagen_nave)

    def update(self):
        self.rect.center = pygame.mouse.get_pos() 

    def draw(self, surface):
        surface.blit(self.imagen_nave, self.rect) 

