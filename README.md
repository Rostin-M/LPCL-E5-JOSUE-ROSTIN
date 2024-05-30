# PensionCalculatorPro

## Por:

Santiago Alzate
Josué Gómez 

## ¿Qué es?

    La calculadora de pensiones es una herramienta digital que ayuda a las personas a estimar el monto de sus pensiones futuras. Utilizando información como la edad actual, el género, el salario actual, las semanas laboradas, el ahorro acumulado, la rentabilidad del fondo de pensiones y la tasa de administración del mismo, esta herramienta proporciona una proyección del ingreso que recibirán durante su jubilación.

## Propósito
    El propósito de la calculadora de pensiones es permitir a los usuarios planificar su futuro financiero durante la jubilación. Al proporcionar una estimación del ingreso futuro, los individuos pueden tomar decisiones informadas sobre ahorros y contribuciones al fondo de pensiones, así como ajustar su planificación financiera para asegurar un retiro cómodo y sin preocupaciones.

## ¿Cómo lo haces funcionar?

### Prerrequisitos para Abrir la Calculadora Pensional

    Antes de comenzar, asegúrate de tener lo siguiente:

1. Tener instalada las últimas versiones de Python y pip disponibles.

2. Para ejecutarlo tienes dos opciones, pero se recomienda el uso de un entorno virtual.
   
    1. Para crear el entorno virtual deberás seguir los siguientes comandos: 
        - <pre>python -m venv my_project</pre>

		- Si estás en Windows ejecuta el siguiente comando:
        <pre>my_project\Scripts\activate</pre>

        - Si estás en MacOS o alguna distribución de Linux:
        <pre>source my_project/bin/activate</pre>

		- Después de tener crear el entorno virtual y activarlo deberías de ver algo similar a esto:
			(my_project) /encryption_engine$
        
        - Una vez creado el entorno, deberás instalar las librerias necesarias para ejecutar el proyecto:
            1. psycopg2 <pre>pip install psycopg2-binary</pre>

            2. En caso que quieras ejecutarlo por interfaz gráfica:
                - Tendrás que instalar kivy, para instalar esta libreria debe de ser por medio de pip (instalador de paquetes de python) ejecute el siguiente comando en la terminal:
					<pre>python -m pip install "kivy[base]"</pre>

                    - Para más información acceder a la documentación oficial: https://kivy.org/doc/stable/gettingstarted/installation.html
            
            3. En caso que desee ejecutar el programa mediante la web:
                - Tendrá que instalar Flask, instalar esta libreria debe de ser por medio de pip (instalador de paquetes de python) ejecute el siguiente comando en la terminal:
					<pre>python -pip install "Flask"</pre>

                    - Para más información acceder a la documentación oficial: https://flask.palletsprojects.com/en/3.0.x/


    3. Puede realizar todo el proceso sin crear un entorno virtual:
        1. Instalar psycopg2 <pre>pip install psycopg2-binary</pre>

        2. En caso que quieras ejecutarlo por interfaz gráfica:
            - Tendrás que instalar kivy, para instalar esta libreria debe de ser por medio de pip (instalador de paquetes de python) ejecute el siguiente comando en la terminal:
                <pre>python -m pip install "kivy[base]"</pre>

                - Para más información acceder a la documentación oficial: https://kivy.org/doc/stable/gettingstarted/installation.html
            
        3. En caso que desee ejecutar el programa mediante la web:
            - Tendrá que instalar Flask, instalar esta libreria debe de ser por medio de pip (instalador de paquetes de python) ejecute el siguiente comando en la terminal:
                <pre>python -pip install "Flask"</pre>

                - Para más información acceder a la documentación oficial: https://flask.palletsprojects.com/en/3.0.x/

    4. Debe tener una base de datos en Neon Tech:
        - Para crearla debes ir a la pagina oficial de Neon Tech: https://neon.tech.

			1. Debes iniciar sesión en su sitio web, o registrarte si no tinenes una cuenta creada.

			2. Creas un nuevo proyecto.
			
			3. Te diriges al apartado que dice "Dashboard".
			
			4. En el apartado Database, selecciona la base de datos donde quieras guardar la base de datos y su información.

			5. Haz click donde dice "ConnectionString", se desplegará un menú.
			
			6. Selecciona la que dice "Parameters only".
			
		- ¿Qué hacer con la información?.

			1. Una vez la página te muestre los parámetros de la base de datos dírigete a la carpeta "src".

			2. Allí deberás entrar a la carpeta "controller".
			
			3. En la carpeta controller, entra al archivo "secret_config_example".
			
			4. Finalmente deberás seguir los pasos indicados en el archivo 'secret_config_example.py' para continuar
			con el proceso de conexión con la base de datos.

### Entradas para calcular la pensión:
 - **Edad actual:** La edad actual del individuo.
 - **Sexo:** El género del individuo (hombre/mujer).
 - **Salario actual:** El salario actual del individuo.
 - **Número de semanas laboradas:** El número de semanas que el individuo ha trabajado.
 - **Ahorro actual:** El monto de ahorro actual del individuo.
 - **Rentabilidad del fondo (%):** La rentabilidad esperada del fondo de pensiones en forma de porcentaje.
 - **Tasa de administración del fondo (%):** La tasa de administración del fondo de pensiones en forma de porcentaje.

### Salidas del cálculo de la pensión:
 - **Valor del ahorro pensional esperado:** El valor estimado del ahorro pensional esperado.
 - **Valor de la pensión anual:** El valor estimado de la pensión anual.
 - **Valor de la pensión mensual:** El valor estimado de la pensión mensual.

## Ejecución:
### Paso a Paso para Abrir la Calculadora Pensional

Aquí tienes los pasos detallados para abrir y utilizar la Calculadora Pensional:

**Opción 1: Descargar desde GitHub:**

1. **Descarga de Archivos:**
   - Descarga el archivo comprimido "PensionCalculatorProBD" desde el enlace proporcionado o desde donde te hayan entregado el archivo.

2. **Extracción de Archivos:**
   - Abre el archivo comprimido "PensionCalculatorProBD-main.zip" utilizando un programa de extracción de archivos, como WinRAR o 7-Zip.
   - Extrae todos los archivos de la carpeta en una ubicación de tu elección en tu computadora.

**Opción 2: Clonar el Repositorio desde Github:**

1. **Clonar el Repositorio:**
   - Abre la terminal o línea de comandos en tu computadora.
   - Navega hasta el directorio donde deseas clonar el repositorio utilizando el comando cd.
   - Utiliza el siguiente comando para clonar el repositorio desde GitHub:

   git clone https://github.com/usuario/PensionCalculatorProBD.git

   Reemplaza usuario por el nombre de usuario de GitHub donde se encuentra el repositorio.


## Conexión a la base de datos:

1. **Accede al sitio web de Neon:**
Ve a Neon.Tech desde tu navegador web.

2. **Regístrate o inicia sesión:**
Si aún no tienes una cuenta, regístrate en la plataforma. De lo contrario, inicia sesión con tus credenciales.

3. **Crea un nuevo proyecto:**
Una vez dentro, crea un nuevo proyecto. Elige un título para el proyecto y nombra la base de datos como "Calculadora_Impuestos".

4. **Accede al panel de control (Dashboard):**
Después de crear el proyecto y la base de datos, ve al panel de control.

5. **Obtén la cadena de conexión:**
En el panel de control, busca la opción de "Connection string" y selecciónala. Luego elige la opción "Parameters only". Esto te proporcionará una cadena de conexión que necesitarás más adelante.

6. **Copia la cadena de conexión:**
Copia todo el contenido del campo de texto proporcionado con la cadena de conexión.

7. **Ubica el archivo SecretConfigSample.py:**
En el repositorio de tu proyecto, busca la carpeta "src" y luego la carpeta "controller". Dentro de esta carpeta, encontrarás un archivo llamado "SecretConfigSample.py".

6. **Pega la cadena de conexión:**
Abre el archivo "SecretConfigSample.py" y pega los parámetros de la cadena de conexión que copiaste en el paso anterior.

7. **Renombra el archivo:**
Por último, cambia el nombre del archivo "SecretConfigSample.py" por "SecretConfig.py". Esto asegurará que el sistema reconozca la configuración de la base de datos.


## Abrir para ejecutar consola:

Para ejecutar el archivo main_consolabd.py desde la terminal, sigue estos pasos:

3. Abre la terminal.
4. Utiliza el comando cd ruta_de_la_carpeta/PensionCalculatorProBD-main

Asegúrate de reemplazar ruta_de_la_carpeta con la ruta real de la carpeta "PensionCalculatorProBD-main" en tu sistema.

5. Una vez en el directorio correcto, puedes ejecutar el archivo main_consolabd.py utilizando Python. Coloca el siguiente comando en tu terminal:
python main_consolabd.py

6. Una vez se te abre la consola en la terminal aparecerá un menú con 7 opciones, el cuál para navegar en él tendrás que seleccionar el número correspondiente a la opción deseada.


7. **Uso de la aplicación:**
- Completa los campos requeridos con la información relevante, como la edad actual, el salario, las semanas laboradas, etc.
- La aplicación mostrará los resultados en pantalla.

8. **Finalización de la Aplicación:**
   - Una vez que hayas utilizado la Calculadora Pensional y obtenido los resultados deseados, puedes cerrar la aplicación seleccionando la opción correspondiente.

 ¡Espero que encuentres útil la aplicación!
   
## Abrir para ejecutar pruebas unitarias:

Para ejecutar el archivo test_bd.py desde la terminal, sigue estos pasos:

3. Abre la terminal.
4. Utiliza el comando cd ruta_de_la_carpeta/PensionCalculatorProBD-main

Asegúrate de reemplazar ruta_de_la_carpeta con la ruta real de la carpeta "PensionCalculatorProBD-main" en tu sistema.

**NOTA:** tener en cuenta que el archivo test_bd.py se encuentra dentro de la carpeta tests.

3. Una vez en el directorio correcto, puedes ejecutar el archivo test_bd.py utilizando Python. Coloca el siguiente comando en tu terminal:
python test_bd.py

## ¿Cómo se integró la base de datos de Neon Tech?
1. Se instala psycopg2 usando el comando: pip install psycopg2.
2. Una vez instalado el controlador, podrás conectarte a tu base de datos desde Python y realizar operaciones como consultas, inserciones, actualizaciones, etc., según sea necesario.

**Bibliotecas Utilizadas:**
El proyecto hace uso de las siguientes bibliotecas estándar de Python:

**unittest:** Utilizada para escribir y ejecutar pruebas unitarias.

**sys:** Biblioteca estándar de Python para manipular el entorno de ejecución del sistema, como la gestión de argumentos de línea de comandos y rutas de acceso.

**psycopg2:** Adaptador de base de datos PostgreSQL para Python, utilizado para conectarse a bases de datos PostgreSQL, ejecutar consultas SQL y manipular datos desde Python.

**Dependencias de Otros Proyectos:**
El proyecto no tiene dependencias externas a otros proyectos. Todas las funcionalidades están implementadas dentro del propio proyecto sin requerir bibliotecas externas.

