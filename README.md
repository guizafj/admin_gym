
# 🏋️‍♂️ Admin Gym Flask

**Admin Gym Flask** es una aplicación web desarrollada con **Flask** para gestionar clientes y operaciones de un gimnasio. Este proyecto fue creado como parte de un curso enfocado en Flask, pero está estructurado de manera que sea simple y sencillo escalarlo y ampliar su utilidad.

---

## 🚀 Características Principales

- 👥 **Gestión de Clientes**: Registro, edición y eliminación de información de clientes.
- 📅 **Control de Membresías**: Seguimiento de membresías activas, fechas de vencimiento y renovaciones.
- 💳 **Pagos y Facturación**: Registro de pagos realizados y generación de facturas.
- 📈 **Reportes**: Generación de reportes sobre asistencia, pagos y estado de membresías.
- 🔐 **Autenticación de Usuarios**: Sistema de login seguro para administradores y empleados.
- 🎨 **Interfaz Intuitiva**: Diseño responsivo y amigable para facilitar la navegación.

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Base de Datos**: MySQL
- **ORM**: SQLAlchemy
- **Control de Versiones**: Git

---

## 📂 Estructura del Proyecto

```
admin_gym_flask/
├── backend/
│   ├── cliente.py
│   ├── cliente_dao.py
│   ├── conexion.py
│   └── formularios.py
├── static/
│   └── css/
├── templates/
├── .env
├── .gitignore
├── LICENSE
├── flaskapp.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/guizafj/admin_gym_flask.git
cd admin_gym_flask
```

### 2. Crear y Activar un Entorno Virtual (opcional)

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instalar las Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto y definir las variables necesarias, por ejemplo:

```env
FLASK_APP=flaskapp.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
DATABASE_URL=mysql://usuario:contraseña@localhost/nombre_base_datos
```

### 5. Inicializar la Base de Datos

```bash
flask db init
flask db migrate -m "Inicialización de la base de datos"
flask db upgrade
```

### 6. Ejecutar la Aplicación

```bash
flask run
```

Accede a la aplicación en [http://localhost:5000](http://localhost:5000)

---

## 📸 Capturas de Pantalla

> *Nota: Aquí se  incluira imágenes o gifs que muestren la interfaz de usuario, como el panel de administración, la gestión de clientes, etc.*

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request describiendo tus cambios.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📬 Contacto

Para consultas o sugerencias:

- **Autor**: [guizafj](https://github.com/guizafj)
- **Correo**: contacto@dguiza