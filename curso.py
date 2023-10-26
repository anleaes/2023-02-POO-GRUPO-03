class Curso:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def __str__(self):
        return f"{self.titulo} ({self.duracao})"
