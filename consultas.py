from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from clases import *

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, nombre de instructor y nombre del departamento


# Se hace una Querty obteniendo Entrega, Tarea, Estudiante, Instructor, Departamento haciendo joins desde Entrega hasta Tarea Donde esta el curso 
# y a partir de el se puede hacer join con Curso y desde Curso hacer Join hasta Instructor para el nombre y Join hasta departamento para poder 
# hacer el filter Para Arte, y join desde Entrega hasta Estudiante para el nombre del estudiante 
entregas = session.query(Entrega).join(Tarea).join(Estudiante).join(Curso).join(Instructor).join(Departamento).filter(Departamento.nombre=='Arte')


# Se muestra lo obtenido de la consulta
for e in entregas:
    print(f"Nombre Tarea: {e.tarea.titulo} - Nombre Estudiante: {e.estudiante.nombre} - Calificacion: {e.calificacion} - Nombre Instructor: {e.tarea.curso.instructor.nombre} - Nombre Curso: {e.tarea.curso.departamento.nombre}")
    print()

# - Calificacion: {e[0].calificacion} - Nombre Instructor: {e[3].nombre} - Departamento: {e[4].nombre}