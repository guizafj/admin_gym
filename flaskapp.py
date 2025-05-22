"""
flaskapp.py

Módulo principal de la aplicación Flask para la gestión de clientes de un gimnasio.
Define las rutas, la lógica de negocio y la integración con los formularios y la base de datos.

Autor: Francisco Diaz Guiza
Fecha: 2025-05-17

Convenciones:
- Se sigue la guía de estilo PEP 8.
- Se documentan funciones y rutas.
"""

from flask import Flask, redirect, render_template, url_for
from backend.cliente import Cliente
from backend.formularios import FormAgregar
from backend.cliente_dao import ClienteDAO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'  # Cambia esto por una clave secreta real

@app.route("/")
@app.route("/index.html")
def index():
    """
    Ruta principal de la aplicación.
    Muestra el formulario para agregar clientes y la lista de clientes existentes.
    """
    app.logger.info("Estas en la página de inicio")
    cliente_db = ClienteDAO.seleccionar()
    if cliente_db is None:
        cliente_db = []  # Asegúrate de que sea una lista vacía si no hay datos
    cliente = Cliente()
    cliente_form = FormAgregar(obj=cliente)
    return render_template("index.html", clientes=cliente_db, forma=cliente_form)

@app.route("/limpiar")
def limpiar():
    """
    Ruta para limpiar el formulario y redirigir a la página de inicio.
    """
    return redirect(url_for('index'))

@app.route("/guardar", methods=["POST"])
def guardar():
    """
    Ruta para guardar o actualizar un cliente.
    Procesa los datos del formulario y realiza la inserción o actualización en la base de datos.
    """
    cliente = Cliente()
    cliente_forma = FormAgregar(obj=cliente)
    if cliente_forma.validate_on_submit():
        cliente_forma.populate_obj(cliente)  # Llena el objeto cliente con los datos del formulario
        if not cliente.id:
            # Si no existe el id, se inserta un nuevo cliente
            ClienteDAO.insertar(cliente)
        else:
            # Si existe el id, se actualiza el cliente
            ClienteDAO.actualizar(cliente)
    return redirect(url_for('index'))

@app.route("/editar/<int:id>")
def editar(id):
    """
    Ruta para editar un cliente existente.
    Carga los datos del cliente en el formulario para su edición.
    
    Args:
        id (int): Identificador del cliente a editar.
    """
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = FormAgregar(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template("index.html", clientes=clientes_db, forma=cliente_forma)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    """
    Ruta para eliminar un cliente.
    
    Args:
        id (int): Identificador del cliente a eliminar.
    """
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('index'))

@app.route("/tabla")
def tabla():
    """
    Ruta para mostrar la tabla de clientes (vista adicional).
    """
    return render_template("tabla.html")

@app.route("/login")
def login():
    """
    Ruta para mostrar la página de login.
    """
    return render_template("login.html")

@app.after_request
def add_header(response):
    """
    Modifica las cabeceras de la respuesta para evitar el almacenamiento en caché.
    """
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == "__main__":
    # Ejecuta la aplicación en modo desarrollo
    app.run(host='0.0.0.0', debug=True)