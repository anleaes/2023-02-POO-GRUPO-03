class Curso:
    def __init__(self, titulo, carga_horaria):
        self.titulo = titulo
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"{self.titulo} ({self.carga_horaria})"
