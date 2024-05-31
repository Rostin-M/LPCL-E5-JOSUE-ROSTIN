from app.models.pension_calculator import Calcular

def calcular_pension(edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion):
    calculo = Calcular(edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
    return calculo.calcular_pension()
