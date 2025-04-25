class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def bankai(self):
        raise NotImplementedError("Bankai não implementada.")

# Exemplo de uso (ainda sem personagem específico)
if __name__ == "__main__":
    p = Personagem("Genérico")
    p.bankai()
