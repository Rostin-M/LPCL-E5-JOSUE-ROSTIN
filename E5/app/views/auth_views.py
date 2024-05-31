from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.database_manager import DatabaseManager

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']

        db_manager = DatabaseManager()

        user_query = "SELECT * FROM usuario WHERE id = %s AND password = %s"
        user_data = db_manager.execute_query_with_params(user_query, (user_id, password))

        if user_data:
            flash('Login successful!')
            session['user_id'] = user_id
            return redirect(url_for('pension.pension_calculator'))
        flash('Invalid user ID or password. Please try again.')
        return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        password = request.form['password']

        db_manager = DatabaseManager()

        # Verificar si el usuario ya existe
        existing_user_query = "SELECT * FROM usuario WHERE id = %s"
        existing_user = db_manager.execute_query_with_params(existing_user_query, (user_id,))

        if existing_user:
            flash('User with this ID already exists.')
            return redirect(url_for('auth.register'))

        # Insertar el nuevo usuario en la base de datos
        insert_user_query = """
            INSERT INTO usuario (id, name, age, gender, password)
            VALUES (%s, %s, %s, %s, %s)
        """
        db_manager.execute_insert_query(insert_user_query, (user_id, name, age, gender, password))

        flash('User registered successfully.')
        return redirect(url_for('auth.login'))  # Redirigir al login o a la página que desees

    return render_template('register.html')

