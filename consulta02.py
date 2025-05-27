from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from clases import *

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 2
# Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . 
# En función de los departamentos, presentar el nombre del departamento y el número de cursos que tiene cada departamento

# Se hace una query haciendo un Join con curso despues a tarea y al final a entrega para poder obtener las calificaciones menor a 0.3
departamentos = session.query(Departamento).join(Curso).join(Tarea).join(Entrega).filter(Entrega.calificacion<=0.3).all()

# Se presenta lo obtenido de la consulta
for d in departamentos:
    print(f"Departamento: {d.nombre} - Numero Cursos: {len(d.cursos)}")