from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.controllers.pension_controller import calcular_pension

pension_bp = Blueprint('pension', __name__)

@pension_bp.route('/pension_calculator', methods=['GET', 'POST'])
def pension_calculator():
    if request.method == 'POST':
        try:
            edad_actual = int(request.form['edad_actual'])
            sexo = request.form['sexo']
            salario_actual = float(request.form['salario_actual'])
            semanas_laboradas = int(request.form['semanas_laboradas'])
            ahorro_actual = float(request.form['ahorro_actual'])
            rentabilidad_fondo = float(request.form['rentabilidad_fondo'])
            tasa_administracion = float(request.form['tasa_administracion'])

            resultado = calcular_pension(edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            return render_template('pension_result.html', resultado=resultado)
        except Exception as e:
            flash(str(e))
    
    return render_template('pension_calculator.html')
