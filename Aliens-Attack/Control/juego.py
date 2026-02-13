import os
import sys
import pygame

from Control.control_nave import Ship
from Control.control_alien import control_alien
from Control.control_laser import controldellaser

class Juego:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 640
        self.WINDOW_HEIGHT = 800

        self.display_surface = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )

        pygame.display.set_caption('Aliens Attack')
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.contador = 0
        
        self.cargar_de_elementos()
        self.conrol_nave = Ship(self)
        self.conrol_laser = controldellaser(self)
        self.conrol_alien = control_alien(self)  
        
        self.ejecutando = True      

    def cargar_de_elementos(self):
        self.fondo = pygame.image.load(os.path.join('Aliens-Attack/imagenes','EspacioFondo.webp'))
        self.fuente = self.fuente = pygame.font.Font('Aliens-Attack/imagenes/04B_30__.TTF', 50)
        self.fuente_chquita = self.fuente_chquita = pygame.font.Font('Aliens-Attack/imagenes/04B_30__.TTF', 20)
        
        self.sonido_laser= pygame.mixer.Sound(
            os.path.join('Aliens-Attack/sonido','laser_sound.mp3')
        )
        self.sonido_laser.set_volume(0.5)
        self.sonido_explosion = pygame.mixer.Sound(
            os.path.join(
                'Aliens-Attack/sonido', 'explosion.mp3'
            )
        )
        self.sonido_explosion.set_volume(0.5)
        
        
        
        
        self.musica= pygame.mixer.Sound(
                os.path.join('Aliens-Attack/sonido','music.mp3')
        )
        self.musica.set_volume(0.7)
        self.musica.play(loops=-1)
        self.fondo = pygame.transform.scale(self.fondo, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    
    def ejecutar(self):
        
        
        self.ejecutar_ventana_de_inicio()
        
        while self.ejecutando:
            self.dt = self.clock.tick(120)/1000
            self.eventos()
            self.consecuencias_eventos()
            self.imagenes_gen()
    
    
    
    def contador_alien(self):
        
        
        
        
        
        
        eliminados_texto = f'Eliminados {self.contador}'
        cargar_texto = self.fuente_chquita.render(eliminados_texto, True, (255,255,255))
        texto_dimension = cargar_texto.get_rect(
            midbottom = (self.WINDOW_WIDTH*1/4, self.WINDOW_HEIGHT -80)
        )
        self.display_surface.blit(cargar_texto, texto_dimension)
        
        pygame.draw.rect(
            self.display_surface,(255,255,255),
            texto_dimension.inflate(30,30),
            width=8,
            border_radius=5
        )
        
    
    
    def contador_tiempo(self):
        
        
        
        tiempo_antes= self.tiempo_menu
        tiempo_ahora = pygame.time.get_ticks()
        contador = (tiempo_ahora - tiempo_antes)//1000
        
        
        tiempo_texto = f'Tiempo: {contador}'
        cargar_texto = self.fuente_chquita.render(tiempo_texto, True, (255,255,255))
        texto_dimension = cargar_texto.get_rect(
            topleft = (self.WINDOW_WIDTH -200 , self.WINDOW_HEIGHT -100)
        )
        self.display_surface.blit(cargar_texto, texto_dimension)
        
        pygame.draw.rect(
            self.display_surface,(255,255,255),
            texto_dimension.inflate(30,30),
            width=8,
            border_radius=5
            
        )
    
    
    
    def imagenes_gen(self):
        self.display_surface.fill((0,0,0))
        
        self.display_surface.blit(self.fondo,(0,0))
        
        self.contador_tiempo()
        self.contador_alien()
        self.conrol_laser.imagen(self.display_surface)
        self.conrol_alien.imagen(self.display_surface)
        self.conrol_nave.draw(self.display_surface)
        pygame.display.update()
    
    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.conrol_laser.evento_disparo(evento)
            self.conrol_alien.evento_alien(evento)
            
    def consecuencias_eventos(self):
        self.conrol_nave.update()
        self.conrol_alien.update()
        self.conrol_laser.update()
        self.revision_colision()
    
    
    def revision_colision (self):
        for alien in self.conrol_alien.lista_alien:
            if self.conrol_nave.rect.colliderect(alien[0]):
                offset = (alien[0].x - self.conrol_nave.rect.x, alien[0].y - self.conrol_nave.rect.y)
                if self.conrol_nave.mask.overlap(self.conrol_alien.mask, offset):
                    pygame.quit()
                    sys.exit()
                
        for laser in self.conrol_laser.lista_laser[:]:
            for alien in self.conrol_alien.lista_alien[:]:
                if laser.colliderect(alien[0]):
                    self.conrol_laser.lista_laser.remove(laser)
                    self.conrol_alien.lista_alien.remove(alien)
                    self.sonido_explosion.play()
                    self.contador =  self.contador + 1
                    
        
        
        
        
    def ejecutar_ventana_de_inicio(self):
        title_font=pygame.font.Font('Aliens-Attack/imagenes/04B_30__.TTF',40)
        start_font=pygame.font.Font('Aliens-Attack/imagenes/04B_30__.TTF',15)
        
        titulo_texto=title_font.render('Aliens Attack', True,(255,255,255))
        texto_inicio=start_font.render('''Para inciar presione "ESPACIO" O "CLICK DERECHO"''',
        True,(255, 255, 0))
        
        
        ubi_texto_titulo = titulo_texto.get_rect(
            midtop = (self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/4))
        
        ubi_texto_inicio= texto_inicio.get_rect(
            midbottom = (self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT*3/4))

        waiting = True
        
        while waiting:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==3:
                    self.tiempo_menu = pygame.time.get_ticks()
                    waiting=False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    self.tiempo_menu = pygame.time.get_ticks()
                    waiting=False
            self.display_surface.fill((0,0,0))
            self.display_surface.blit(self.fondo, (0, 0))

            
            self.display_surface.blit(titulo_texto,ubi_texto_titulo)
            self.display_surface.blit(texto_inicio,ubi_texto_inicio)

            pygame.display.update()
            self.clock.tick(60)


        