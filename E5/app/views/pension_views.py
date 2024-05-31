from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.models.database_manager import DatabaseManager
from app.controllers.pension_controller import calcular_pension
from app.models.database_manager import DatabaseManager

pension_bp = Blueprint('pension', __name__)

@pension_bp.route('/pension_calculator', methods=['GET', 'POST'])
def pension_calculator():
    if request.method == 'POST':
        # Obtener el ID de usuario de la sesión
        user_id = session.get('user_id')

        if user_id is None:
            flash('Error: No se ha iniciado sesión.')
            return redirect(url_for('login'))  # Redirigir al inicio de sesión si no hay un usuario autenticado

        db_manager = DatabaseManager()

        # Obtener datos del usuario actual
        user_data = db_manager.execute_query_with_params("SELECT age, gender FROM usuario WHERE id = %s", (user_id,))
        if not user_data:
            flash('Error: No se pudo obtener la información del usuario.')
            return redirect(url_for('pension.pension_calculator'))

        age, gender = user_data[0]  # Suponiendo que el resultado es una lista de tuplas de un solo elemento

        # Obtener otros datos del formulario
        salario_actual = float(request.form['current_salary'])
        semanas_laboradas = int(request.form['worked_weeks'])
        ahorro_actual = float(request.form['current_savings'])
        rentabilidad_fondo = float(request.form['fund_profitability'])
        tasa_administracion = float(request.form['administration_fee'])

        # Realizar los cálculos necesarios para la pensión
        result = calcular_pension(age, gender, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        print(result)
        
        # Redirigir a la vista de resultados con los datos calculados
        return redirect(url_for('pension.pension_result', resultado=result))

    else:
        # Renderizar la plantilla de la calculadora de pensiones en caso de un GET
        return render_template('pension_calculator.html')

@pension_bp.route('/pension_result', methods=['GET', 'POST'])
def pension_result():
    resultado = request.args.get('resultado')
    print(resultado)
    print("-----")
    if request.method == 'GET':
        resultado = request.args.get('resultado')
        if resultado:
            return render_template('pension_result.html', resultado=resultado)
        else:
            flash('Error: No se encontraron resultados.')
            return redirect(url_for('pension.pension_calculator'))
    
    elif request.method == 'POST':

        db_manager = DatabaseManager()  # Instancia de tu gestor de base de datos

        # Guardar los resultados en la base de datos
        query = "INSERT INTO pension_results (expected_pension_savings, annual_pension_value, monthly_pension_value) VALUES (%s, %s, %s)"
        params = (resultado[0], resultado[1], resultado[2])
        db_manager.execute_insert_query(query, params)
        db_manager.close_connection()
        
        flash('Resultados guardados en la base de datos.')
        return redirect(url_for('pension.pension_result'))

    return render_template('pension_result.html')

