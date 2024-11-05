from books.models import Autor, Editorial, Libro, Contacto

# Crea autores
autor1 = Autor.objects.create(nombre="Gabriel", apellido="García Márquez", fecha_nacimiento="1927-03-06", biografia="Autor de Cien Años de Soledad.")
autor2 = Autor.objects.create(nombre="J.K.", apellido="Rowling", fecha_nacimiento="1965-07-31", biografia="Creadora del mundo de Harry Potter.")
autor3 = Autor.objects.create(nombre="George", apellido="Orwell", fecha_nacimiento="1903-06-25", biografia="Conocido por su novela 1984.")

# Crea editoriales
editorial1 = Editorial.objects.create(nombre="Editorial Sudamericana", direccion="Calle Falsa 123", ciudad="Buenos Aires", pais="Argentina")
editorial2 = Editorial.objects.create(nombre="Bloomsbury Publishing", direccion="50 Bedford Square", ciudad="Londres", pais="Reino Unido")
editorial3 = Editorial.objects.create(nombre="Secker & Warburg", direccion="Random House", ciudad="Londres", pais="Reino Unido")

# Crea libros
libro1 = Libro.objects.create(titulo="Cien Años de Soledad", fecha_publicacion="1967-05-30", editorial=editorial1, isbn="9788437604947")
libro1.autores.add(autor1)  # Relación muchos a muchos (agregamos el autor al libro)

libro2 = Libro.objects.create(titulo="Harry Potter y la Piedra Filosofal", fecha_publicacion="1997-06-26", editorial=editorial2, isbn="9780747532699")
libro2.autores.add(autor2)  # Relación muchos a muchos

libro3 = Libro.objects.create(titulo="1984", fecha_publicacion="1949-06-08", editorial=editorial3, isbn="9780451524935")
libro3.autores.add(autor3)  # Relación muchos a muchos