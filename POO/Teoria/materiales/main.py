
from aves import Golondrina
from aves import pepita, anastasia, roberta, juanita, chimuelo, hipo
#cuando los objetos hacen o pueden hacer algo en ppio no tienen porque responder

# print (pepita.volar_en_circulos())
#cuando el objeto conoce la operacion que le pedimos no tira error

# print (pepita.cantar_boleros())
#pepita no sabe cantar boleros, y nos dimos cuenta porque tira error. es decir que pepita no tiene el atributo cantar_boleros()
#los mensajes se usan haciendo: .mensaje()
# un mensaje es un metodo
#print (pepita.energia)
#print (pepita.comer_alpiste(1))
# necesita un argumento para saber que cantidad comer de alpiste

#print (pepita.energia)
#print (pepita.volar_en_circulos())
#print (pepita.energia)

#aprendimos que los objetos tienen estados, en el caso de pepita es la energía.

# eso que pasa cuando pepita cambia su estado es lo que se conoce como comportamiento de los objetos
#print (anastasia == pepita)
# no son el mismo objeto y por lo tanto los objetos tienen identidad
# dos objetos distintos son instancias de distinas de una clase.
#print (anastasia.energia)
#print (anastasia.comer_alpiste(2))
#print (anastasia.energia)

#print (anastasia)
# vemos que tipo de pajaro es anastasia
# golondrina --> una clase.
# pepita --> un objeto.

#print (anastasia.comer_alpiste(10))
#print (anastasia.energia)
#print (anastasia.volar_en_circulos())
#print (anastasia.energia)

#importamos a roberta
# print (roberta)
# #roberta es un dragon
# print (roberta.energia)
# print (roberta.escupir_fuego())
# print (roberta.energia)
# print (roberta == anastasia)

# print (roberta.comer_peces(10))
# print (roberta.energia)

# print (roberta.cantidad_dientes)

# cada clase tiene su interfaz.
# donde la interfaz es el conjubnto de mensajes que entiende

# print (pepita.esta_feliz())

### Equipo 

#print (hipo)
#print (hipo.equipo)
#print (hipo.el_equipo())

#print (hipo.agregar_animal(chimuelo))

#print (hipo.equipo)

# print ("energia chimuelo",chimuelo.energia)

print (pepita.volar(11))
