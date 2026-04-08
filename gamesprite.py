from pygame import transform, image, sprite, draw

class GameSprite(sprite.Sprite):
  def __init__(self, ruta, cor_x, cor_y, ancho, alto, girar = False):
    super().__init__()
    self.imagen = transform.scale(image.load(ruta), (ancho, alto))
    self.rect = self.imagen.get_rect()
    self.rect.x = cor_x
    self.rect.y = cor_y
    if girar:
      self.imagen = transform.rotate(self.imagen, 90)
      self.rect.width = alto
      self.rect.height = ancho

    
    
  def pintar(self, my_window, colision = False, color = (255,0,0)):
    my_window.blit(self.imagen, (self.rect.x, self.rect.y))
    if colision: draw.rect(my_window, color, self.rect, 2)