import pygame
from gamesprite import GameSprite
from player import Player
from random import randint

pygame.init()
pantalla = pygame.display.set_mode((800,500))
pygame.display.set_caption("Minecraft")
clock = pygame.time.Clock()
icono = pygame.image.load("./assets/minecraft_94415.png")
pygame.display.set_icon(icono)
fondo = GameSprite("assets/fondo.png", 0, 0, 800, 500)
suelo = GameSprite("assets/bloques_bedrock.png", -1, 459, 800, 70)
limite_derecho = GameSprite("assets/bloques_bedrock.png", 800, -60, 500, 50, True)
limite_izquierdo = GameSprite("assets/bloques_bedrock.png", -50, -60, 500, 50, True)
limite_cielo = GameSprite("assets/bloques_bedrock.png", -1, -130, 800, 70)
steve = Player("./assets/steve.png",50, 100, 60, 120)

limites = [suelo, limite_izquierdo, limite_derecho, limite_cielo]

cubos = []
y = 410
for i in range(2):
  x = 0
  for j in range(16):
    if i < 1 or randint(0,15) < 6:
      cubos.append(GameSprite("assets/tierra_cubo.jpg", x, y, 50, 50))
    x += 50
  y -= 50
tierra1 = GameSprite("assets/tierra_cubo.jpg", 350, 0, 50, 50)
tierra2 = GameSprite("assets/tierra_cubo.jpg", 410, 0, 50, 50)
tierra3 = GameSprite("assets/tierra_cubo.jpg", 410, 0, 50, 50)
def actualizar_colisiones():
  list_colisiones = []
  for limite in limites:
    list_colisiones.append(limite.rect)
  for cubo in cubos:
    list_colisiones.append(cubo.rect)
  return list_colisiones



run = True
while run:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      run = False
    elif evento.type == pygame.KEYDOWN:
      if evento.key == pygame.K_d: steve.mover(5)
      elif evento.key == pygame.K_a: steve.mover(-5)
      elif evento.key == pygame.K_w:
        steve.saltar()
    elif evento.type == pygame.KEYUP:
      if evento.key == pygame.K_d or evento.key == pygame.K_a: steve.mover(0)
      elif evento.key == pygame.K_w:
        steve.saltar()
    if evento.type == pygame.MOUSEBUTTONDOWN:
      if evento.button == 1:
        x, y = pygame.mouse.get_pos()
        for cubo in cubos:
          if cubo.rect.collidepoint(x, y):
            cubos.remove(cubo)
            break
      elif evento.button == 3:
        x, y = pygame.mouse.get_pos()

        tam = 50
        x = (x // tam) * tam
        y = (y // tam) * tam

        nuevo_rect = pygame.Rect(x, y, tam, tam)

        ocupado = False

        for cubo in cubos:
            if cubo.rect == nuevo_rect:
                ocupado = True
                break

        for limite in limites:
            if limite.rect == nuevo_rect:
                ocupado = True
                break

        if nuevo_rect.colliderect(steve.rect):
            ocupado = True

        if not ocupado:
            cubos.append(GameSprite("assets/tierra_cubo.jpg", x, y, tam, tam))
            list_colisiones = actualizar_colisiones()
  
    
  lista_colisiones = actualizar_colisiones()
  steve.actualizar(lista_colisiones)
  
  fondo.pintar(pantalla)
  for limite in limites: limite.pintar(pantalla)

  for cubo in cubos: cubo.pintar(pantalla)
  steve.pintar(pantalla)

  clock.tick(40)
  pygame.display.update()

