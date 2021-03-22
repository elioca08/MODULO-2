from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm.exc import NoResultFound


engine = create_engine('sqlite:///words.db')
Session =sessionmaker(engine)
session = Session()

Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'

    palabra = Column('palabra', String(50), primary_key = True )
    significado = Column('significado',String(50))

  


print("Escoger una opción")
print("A.Agregar nueva palabra")
print("B.Editar palabra")
print("C.ELiminar palabra")
print("D.Buscar significado de palabra")
print("E.Mostrar palabras")

opc = str(input("Elegir "))

Session = sessionmaker(engine)

session = Session()


if opc == 'A':
  p = input("Escribir la palabra que desea añadir: ")
  s = input("Escribir el significado de la palabra: ")
  w=Word()
  w.palabra = p
  w.significado = s
  session.add(w)
  session.commit()

if opc == 'B':
  w = input("Ingresar la palabra que desea cambiar: ")
  p = input("Ingresar la nueva palabra: ")
  s = input("Ingresar el significado de la nueva palabra: ")
  resultado = session.query(Word).filter(Word.palabra == w).update({Word.palabra: p, Word.significado: s})
  session.commit()

if opc == 'C':
  w = input("Escribir la palabra que desea eliminar: ")
  resultado = session.query(Word).filter(Word.palabra == w).delete()
  session.commit()


if opc == 'D':
  w = input("Ingresar la palabra que desea buscar ")
  try:
   resultado = session.query(Word).filter(Word.palabra == w).one()
   print(resultado.palabra,'=', resultado.significado)
  except NoResultFound as err:
    print("No se encuentra la palabra")

if opc == 'E': 
 resultado = session.query(Word).all()
 for i in resultado:
  print(i.palabra,'=', i.significado)


Base.metadata.create_all(engine)





