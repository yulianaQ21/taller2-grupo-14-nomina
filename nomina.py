""""Desarrollar un programa en el lenguaje de programación PYTHON que calcule el salario neto de un empleado 
en Colombia, teniendo en cuenta los descuentos obligatorios y beneficios establecidos por la ley. 

qué necesito:nombre, salario,dias trabajados,auxilio de transporte, descuentos aplicados(salud, pension, retefuente).
fórmulas: salarioDiario= salarioBásicoMensual/30 ,salarioDevengado= salarioDiario*diasTrabajados
salarioNeto: salarioDevengado + auxilioTransporte - (salud + pension +retefuente) 
auxilioTransporte= ?? salarioDevengado <= 2 * 
retefuente= ?? salarioDevengado >= 4.731.000
descuentoSalud= salarioDevengado * 4 /100
descuentoPension= salarioDevengado * 4 / 100

qué muestro: Nombre del empleado,Salario devengado ,Auxilio de transporte,
Descuentos aplicados (salud, pensión, retención en la fuente), Salario neto a pagar,
Total pagado por subsidio transporte, Total descontado para pensión,   Total descontado para salud 
Total de la nomina pagada 

""" 
#variables
nombreEmpleado= ""
salarioDevengado= 0
diasTrabajados= 0
salud= 0
pension= 0
retefuente= 0
salarioNeto= 0

#constantes
auxilioTransporte=162000
salarioMinimo= 1423500

#entradas
nombreEmpleado= input("ingrese el nombre de el empleado:")
diasTrabajados= int(input("ingrese los dias trabajados:"))

#procesos
salarioDiario= salarioMinimo / 30
salarioDevengado= salarioDiario * diasTrabajados 
salarioNeto= salarioDevengado + auxilioTransporte - (salud + pension +retefuente)
descuentoSalud= salarioDevengado * 4 /100
descuentoPension= salarioDevengado * 4 / 100





    

    
    
 
 
