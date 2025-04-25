# App Flask - Zona Fit Gym

Este proyecto es una aplicación web desarrollada con Flask para gestionar clientes de un gimnasio.
Se hace como forma de un curso enfocado en flask, pero esta estructurado de manera que sea simple 
y sencillo escalarlo y ampliar su utilidad

## Requisitos

- Python 3.8 o superior
- MySQL
- Entorno virtual (opcional)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/guizafj/admin_gym.git
   cd tu-repositorio

2. Crea un entorno virtual (opcional):
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias:
    pip install -r requirements.txt

4. Configura el archivo .env: 
    Crea un archivo .env en la raíz del proyecto basado en .env.example y agrega  
    tus credenciales de base de datos.

5. Ejecuta la aplicación:
    python flaskapp.py

6. Abre tu navegador en:
     http://127.0.0.1:5000

## Estructura del proyecto

    app_flask/
    ├── backend/
    │   ├── cliente.py
    │   ├── cliente_dao.py
    │   ├── conexion.py
    │   └── formularios.py
    ├── static/
    │   └── css/
    │       └── styles.css
    ├── templates/
    │   ├── base.html
    │   └── index.html
    ├── flaskapp.py
    ├── .env.example
    ├── requirements.txt
    └── README.md

