def calcular_salario_neto(nombre_empleado, salario_bruto):
    # Porcentajes establecidos por la ley colombiana
    descuento_salud = 0.04  # 4% para salud
    descuento_pension = 0.04  # 4% para pensión
    
    # Umbral del salario mínimo (en pesos colombianos, ajusta si es necesario)
    salario_minimo = 1160000  # Salario mínimo legal vigente (2025, ejemplo)
    auxilio_transporte = 140606  # Auxilio de transporte (2025, ejemplo)
    
    # Cálculo del auxilio de transporte (aplica si el salario bruto <= 2 salarios mínimos)
    if salario_bruto <= 2 * salario_minimo:
        beneficio_transporte = auxilio_transporte
    else:
        beneficio_transporte = 0
    
    # Cálculo de los descuentos
    deduccion_salud = salario_bruto * descuento_salud
    deduccion_pension = salario_bruto * descuento_pension
    deduccion_total = deduccion_salud + deduccion_pension
    
    # Salario neto
    salario_neto = salario_bruto - deduccion_total + beneficio_transporte
    
    # Resultados
    print(f"Empleado: {nombre_empleado}")
    print("Salario bruto: ${:.2f}".format(salario_bruto))
    print("Descuento por salud (4%): ${:.2f}".format(deduccion_salud))
    print("Descuento por pensión (4%): ${:.2f}".format(deduccion_pension))
    print("Total descuentos: ${:.2f}".format(deduccion_total))
    print("Auxilio de transporte: ${:.2f}".format(beneficio_transporte))
    print("Salario neto: ${:.2f}".format(salario_neto))

# Ejemplo de uso:
nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
calcular_salario_neto(nombre_empleado, salario_bruto)