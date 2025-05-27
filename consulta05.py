from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from clases import *

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 5
# 5.1 En una consulta, obtener todos los cursos.
# 5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso (con otra consulta), 
# y presentar el promedio de calificaciones de las entregas


# Se obtienen todos los cursos
cursos = session.query(Curso).all()

for c in cursos:
    # Se obtiene el promedio con la funcion "func" para poder sacar el avg y se le filtra segun el id del curso
    promedio = session.query(func.avg(Entrega.calificacion)).join(Tarea).filter(Tarea.curso_id == c.id).all()
    print(f"Curso: {c.titulo} - Promedio: {promedio[0]}")