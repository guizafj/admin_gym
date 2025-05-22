"""
cliente_dao.py

Módulo Data Access Object (DAO) para la entidad Cliente.
Permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre la tabla 'clientes' en la base de datos.

Autor: Francisco Diaz Guiza
Fecha: 2025-05-17

Convenciones:
- Se sigue la guía de estilo PEP 8.
- Se documentan clases y métodos.
"""

from backend.conexion import Conexion
from backend.cliente import Cliente

class ClienteDAO:
    """
    DAO para la entidad Cliente.
    Encapsula la lógica de acceso a datos para la tabla 'clientes'.
    """

    SELECCIONAR = "SELECT * FROM clientes ORDER BY id"
    SELECCIONAR_ID = "SELECT * FROM clientes WHERE id=%s"
    INSERT = "INSERT INTO clientes (nombre, apellido, membresia) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM clientes WHERE id=%s"

    def __init__(self):
        """Constructor vacío, no requiere inicialización."""
        pass

    @classmethod
    def seleccionar(cls):
        """
        Recupera todos los clientes de la base de datos.

        Returns:
            list: Lista de objetos Cliente.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                # registro: (id, nombre, apellido, membresia)
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Ocurrió un error al seleccionar los clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_por_id(cls, id):
        """
        Recupera un cliente por su ID.

        Args:
            id (int): ID del cliente a buscar.

        Returns:
            Cliente: Objeto Cliente si se encuentra, None en caso contrario.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            if registro:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                return cliente
            return None
        except Exception as e:
            print(f"Ocurrió un error al seleccionar un cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        """
        Inserta un nuevo cliente en la base de datos.

        Args:
            cliente (Cliente): Objeto Cliente a insertar.

        Returns:
            int: Número de filas afectadas.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al insertar el cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        """
        Actualiza los datos de un cliente existente.

        Args:
            cliente (Cliente): Objeto Cliente con los datos actualizados.

        Returns:
            int: Número de filas afectadas.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al actualizar el cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        """
        Elimina un cliente de la base de datos.

        Args:
            cliente (Cliente): Objeto Cliente a eliminar (se usa el atributo id).

        Returns:
            int: Número de filas afectadas.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al eliminar el cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

