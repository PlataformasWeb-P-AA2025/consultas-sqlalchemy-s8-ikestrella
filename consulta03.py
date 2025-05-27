from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from clases import *

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 3
#    Obtener todas las tareas asignadas a los siguientes estudiantes 
#    Jennifer Bolton 
#    Elaine Perez
#    Heather Henderson
#    Charles Harris
#    En función de cada tarea, presentar el número de entregas que tiene


# Se hace una Query de tarea donde se hace un join con Estudiante y se filtra segun el nombre del Estudiante de (Charles Harris, Heather Henderson, Elaine Perez, Jennifer Bolton)
tareas = session.query(Tarea).join(Entrega).join(Estudiante).filter(or_(Estudiante.nombre=='Jennifer Bolton', Estudiante.nombre=='Elaine Perez', Estudiante.nombre=='Heather Henderson', Estudiante.nombre=='Charles Harris')).all()

# Se presenta lo obtenido de la query donde en len se muestra la cantidad de entregas para esos estudiantes filtrados que hay para esa tarea
for t in tareas:
    print(f"Tareas: {t.titulo} - Numero de Entregas: {len(t.entregas)}")