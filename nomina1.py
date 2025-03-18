import colorama
from colorama import Fore, Style

def validar_entrada (mensaje, tipo=float, min_val=0, max_val=8000000):
    while True:
        try:
            valor = tipo(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(Fore.RED + f"Error: Ingresa un valor entre {min_val} y {max_val}." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Error: Ingresa un número válido." + Style.RESET_ALL)

def calcular_salario_devengado(salario_base, dias_trabajados):
    return (salario_base / 30) * dias_trabajados

def calcular_auxilio_transporte(salario_base, smlv, auxilio):
    return auxilio if salario_base < (2 * smlv) else 0

def calcular_descuentos(salario_devengado, retencion_fuente=0):
    salud = salario_devengado * 0.04
    pension = salario_devengado * 0.04
    retencion = salario_devengado * (retencion_fuente / 100) if retencion_fuente > 0 else 0
    return salud, pension, retencion

def calcular_salario_neto(salario_devengado, auxilio, salud, pension, retencion):
    return salario_devengado + auxilio - (salud + pension + retencion)

def main():
    colorama.init()
    SMLV = 1300000  # Salario mínimo legal vigente (ejemplo)
    AUXILIO_TRANSPORTE = 162000  # Auxilio de transporte
    UMBRAL_RETENCION = 4000000  # Umbral para aplicar retención
    
    total_nomina = 0
    total_auxilio = 0
    total_descuento_salud = 0
    total_descuento_pension = 0
    
    while True:
        print(Fore.CYAN + "\n--- Cálculo de Salario ---" + Style.RESET_ALL)
        nombre = input("Nombre del empleado: ")
        salario_base = validar_entrada("Salario básico mensual: ")
        dias_trabajados = validar_entrada("Días trabajados en el mes: ", int, 1, 30)
        retencion_fuente = validar_entrada("Porcentaje de retención en la fuente (0 si no aplica): ", float, 0, 100)
        
        salario_devengado = calcular_salario_devengado(salario_base, dias_trabajados)
        auxilio = calcular_auxilio_transporte(salario_base, SMLV, AUXILIO_TRANSPORTE)
        salud, pension, retencion = calcular_descuentos(salario_devengado, retencion_fuente)
        salario_neto = calcular_salario_neto(salario_devengado, auxilio, salud, pension, retencion)
        
        print(Fore.GREEN + f"\nEmpleado: {nombre}" + Style.RESET_ALL)
        print(f"Salario devengado: {salario_devengado:,.2f}")
        print(f"Auxilio de transporte: {auxilio:,.2f}")
        print(f"Descuento salud: {salud:,.2f}")
        print(f"Descuento pensión: {pension:,.2f}")
        print(f"Retención en la fuente: {retencion:,.2f}")
        print(Fore.YELLOW + f"Salario neto: {salario_neto:,.2f}" + Style.RESET_ALL)
        
        total_nomina += salario_neto
        total_auxilio += auxilio
        total_descuento_salud += salud
        total_descuento_pension += pension
        
        continuar = input("¿Desea calcular otro salario? (Sí/No): ").strip().lower()
        if continuar != "si":
            break
    
    print(Fore.MAGENTA + "\n--- Resumen Total de Nómina ---" + Style.RESET_ALL)
    print(f"Total nómina pagada: {total_nomina:,.2f}")
    print(f"Total pagado por auxilio de transporte: {total_auxilio:,.2f}")
    print(f"Total descontado para salud: {total_descuento_salud:,.2f}")
    print(f"Total descontado para pensión: {total_descuento_pension:,.2f}")
