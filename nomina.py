""""Desarrollar un programa en el lenguaje de programación PYTHON que calcule el salario neto de un empleado 
en Colombia, teniendo en cuenta los descuentos obligatorios y beneficios establecidos por la ley. 

qué muestro: Nombre del empleado,Salario devengado ,Auxilio de transporte,
Descuentos aplicados (salud, pensión, ), Salario neto a pagar,
Total pagado por subsidio transporte, Total descontado para pensión,   Total descontado para salud 
Total de la nomina pagada 

""" 

#variables
nombre= ""
salarioBasico=0
salarioDevengado= 0
diasTrabajados= 0
descuentoSalud= 0.04 #4%
descuentoPension= 0.04 #4%
salarioNeto= 0
deduccionTotal=0

#constantes
auxilioTransporte= 162000 #auxilio de tranasporte Colombia

#calculo salario

def calcularSalarioDevengado(salarioBasico, diasTrabajados):
    salarioDevengado = (salarioBasico / 30) * diasTrabajados
    return salarioDevengado

def calcularDescuentoSalud(salarioDevengado):
    descuentoSalud = salarioDevengado * 0.04
    return descuentoSalud

def calcularDescuentoPension(salarioDevengado):
    descuentoPension = salarioDevengado * 0.04
    return descuentoPension

def calcularDeduccionTotal(descuentoSalud, descuentoPension):
    deduccionTotal = descuentoSalud + descuentoPension
    return deduccionTotal

def calcularSalarioNeto(salarioDevengado, auxilioTransporte, deduccionTotal):
    salarioNeto = salarioDevengado + auxilioTransporte - deduccionTotal
    return salarioNeto

# Cálculos
salarioDevengado = salarioBasico + diasTrabajados
descuentoSalud = salarioDevengado * descuentoSalud
descuentoPension = salarioDevengado * descuentoPension
deduccionTotal = descuentoSalud+ descuentoPension
salarioNeto = salarioDevengado+ auxilioTransporte - deduccionTotal


# Cálculo del auxilio de transporte (aplica si el salario devengado <= 2 salarios mínimos)
if salarioDevengado <= 2 * salarioBasico:
        auxilioTransporte = auxilioTransporte
else:
        auxilioTransporte = 0
        
def validar_salario(salario):
    if salarioBasico > 0 and salarioBasico <= 8000000:
        return print(salarioBasico)
    else:
        return print("ERROR: ingrese in valor entre 0 - 8000000")        


# entradas 
nombreEmpleado = input("Ingrese el nombre: ")
diasTrabajados= int(input("ingrese los días trabajados:"))
salarioBasico = float(input("Ingrese el salario: "))
    
     
# Salidas
print(f"Empleado: {nombreEmpleado}")
print(f"dias trabajados: {diasTrabajados}")
print(f"Auxilio de transporte: {auxilioTransporte}")
print(f"Salario neto: {salarioNeto:,.2f}")
print(f"Salario devengado: {salarioDevengado}")
print(f"Descuento salud: {descuentoSalud}")
print(f"Descuento pensión: {descuentoPension}")
print(f"Deducción total: {deduccionTotal}")
print(f"Salario neto: {salarioNeto}")