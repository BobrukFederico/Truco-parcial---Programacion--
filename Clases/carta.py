class Carta:
    def __init__(self, numero: int, palo: str, valor: int = 0, valor_envido: int = 0):
        self.numero = numero
        self.palo = palo
        self.valor = valor
        self.ruta_imagen = self.imagen_carta()

    #@property
    def numero(self) -> int:
        '''
        Devuelve el numero de la carta
        '''
        return self.numero
    
    #@property
    def palo(self) -> str:
        '''
        Devuelvo el tipo de la carta
        '''
        return self.palo
    
    def valor(self) -> int:
        return self.valor
    
    def imagen_carta(self):
        return f"cartas_perso/{self.numero} de {self.palo}.png"