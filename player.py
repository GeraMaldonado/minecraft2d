from gamesprite import GameSprite

class Player(GameSprite):
    def __init__(self, ruta, cor_x, cor_y, ancho, alto):
        super().__init__(ruta, cor_x, cor_y, ancho, alto)
        self.speedx = 0
        self.speedy = 0
        self.en_suelo = False
        self.gravedad_fuerza = 1
        self.salto_fuerza = -13
        self.max_caida = 15

    def mover(self, x):
        self.speedx = x

    def saltar(self):
        if self.en_suelo:
            self.speedy = self.salto_fuerza
            self.en_suelo = False

    def aplicar_gravedad(self):
        self.speedy += self.gravedad_fuerza
        if self.speedy > self.max_caida:
            self.speedy = self.max_caida

    def mover_horizontal(self, bloques):
        self.rect.x += self.speedx

        for bloque in bloques:
            if self.rect.colliderect(bloque):
                if self.speedx > 0:
                    self.rect.right = bloque.left
                elif self.speedx < 0:
                    self.rect.left = bloque.right

    def mover_vertical(self, bloques):
        self.rect.y += self.speedy
        self.en_suelo = False

        for bloque in bloques:
            if self.rect.colliderect(bloque):
                if self.speedy > 0:
                    self.rect.bottom = bloque.top
                    self.speedy = 0
                    self.en_suelo = True
                elif self.speedy < 0:
                    self.rect.top = bloque.bottom
                    self.speedy = 0

    def actualizar(self, bloques):
        self.mover_horizontal(bloques)
        self.aplicar_gravedad()
        self.mover_vertical(bloques)