
class Pelicula:
    def __init__(self, titulo, genero, año_lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self.año_lanzamiento = año_lanzamiento

    def __str__(self):
        return f"{self.titulo} ({self.año_lanzamiento}) - Género: {self.genero}"


class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = []

#Agregar pelicula
    def agregar_pelicula(self, titulo, genero, año_lanzamiento):
        nueva = Pelicula(titulo, genero, año_lanzamiento)
        self.peliculas.append(nueva)
        print(f"Película '{titulo} {genero} {año_lanzamiento}' agregada correctamente.")

#Mostar catalogo
    def mostrar_catalogo(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            print("\n Catálogo de Películas:")
            for p in self.peliculas:
                print(f"- {p}")

#filtro por titulo
    def buscar_por_titulo(self, titulo):
        resultados = [p for p in self.peliculas if p.titulo.lower() == titulo.lower()]
        if resultados:
            print("\n Película encontrada:")
            for p in resultados:
                print(f"- {p}")
        else:
            print(f" No se encontró ninguna película con el título '{titulo}'.")

#filtro por genero
    def filtrar_por_genero(self, genero):
        resultados = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if resultados:
            print(f"\n Películas del género '{genero}':")
            for p in resultados:
                print(f"- {p}")
        else:
            print(f"No hay películas del género '{genero}'.")
