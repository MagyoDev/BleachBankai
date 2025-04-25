class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def bankai(self):
        raise NotImplementedError("Bankai não implementada.")

class Ichigo(Personagem):
    def bankai(self):
        print(f"{self.nome} ativa Tensa Zangetsu! Velocidade e ataque aumentados drasticamente!")

if __name__ == "__main__":
    ichigo = Ichigo("Ichigo Kurosaki")
    ichigo.bankai()
