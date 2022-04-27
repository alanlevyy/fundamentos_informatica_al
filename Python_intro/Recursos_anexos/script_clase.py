def division(numero, divisor):
    try:
        return(numero/divisor)
    except ZeroDivisionError:
       print("Ops!Hoy estoy quemada")

print(division(6,3))



