from flask import Flask, redirect, render_template, url_for
from backend.cliente import Cliente
from backend.formularios import FormAgregar
from backend.cliente_dao import ClienteDAO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'  # Cambia esto por una clave secreta real

@app.route("/")
@app.route("/index.html")
def index():
    app.logger.info("Estas en la pagina de inicio")    
    # Se recuperan los datos de la base de datos
    cliente_db = ClienteDAO.seleccionar()
    # Crear un objeto de formulario
    cliente = Cliente()
    cliente_form = FormAgregar(obj=cliente)
    return render_template("index.html", clientes = cliente_db, forma=cliente_form)

@app.route("/limpiar")
def limpiar():
    return redirect(url_for('index'))

@app.route("/guardar", methods=["POST"])
def guardar():
    # se recuperan los datos del formulario
    cliente = Cliente()
    cliente_forma = FormAgregar(obj=cliente)
    if cliente_forma.validate_on_submit():
        # se llena el objeto cliente con los datos del formulario
        cliente_forma.populate_obj(cliente) # Aqui se recuper el id tambien
        if not cliente.id:
            # si no existe el id, se asigna un nuevo id
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente) # En este caso se actualiza el cliente
        # se guarda el cliente en la base de datos
        ClienteDAO.insertar(cliente)
    # Redireccionar a la página de inicio
    return redirect(url_for('index'))

@app.route("/editar/<int:id>") # se usa  la url base/editar/id
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = FormAgregar(obj=cliente)
    # Recuperar el lista de clientes
    clientes_db = ClienteDAO.seleccionar()
    return render_template("index.html", clientes=clientes_db, forma=cliente_forma)

@app.route("/eliminar/<int:id>") # se usa  la url base/eliminar/id
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)   
    # Redireccionar a la página de inicio
    return redirect(url_for('index'))


@app.route("/tabla")
def tabla():
    return render_template("tabla.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)