class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def bankai(self):
        raise NotImplementedError("Bankai não implementada.")

class Ichigo(Personagem):
    def bankai(self):
        print(f"{self.nome} ativa Tensa Zangetsu! Velocidade e ataque aumentados drasticamente!")

class Byakuya(Personagem):
    def bankai(self):
        print(f"{self.nome} ativa Senbonzakura Kageyoshi! Milhares de lâminas voam em direção ao inimigo!")

class Hitsugaya(Personagem):
    def bankai(self):
        print(f"{self.nome} ativa Daiguren Hyorinmaru! O inimigo começa a ser congelado!")

def simular_batalha():
    personagens = [
        Ichigo("Ichigo Kurosaki"),
        Byakuya("Byakuya Kuchiki"),
        Hitsugaya("Tōshirō Hitsugaya")
    ]
    for p in personagens:
        p.bankai()

if __name__ == "__main__":
    simular_batalha()
