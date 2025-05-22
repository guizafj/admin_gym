"""
cliente.py

Define la clase Cliente, que representa la entidad cliente del sistema.
Incluye atributos privados y propiedades para acceder y modificar los datos de forma controlada.

Autor: Francisco Diaz Guiza
Fecha: 2025-05-17

Convenciones:
- Se sigue la guía de estilo PEP 8.
- Se documentan clases y métodos.
"""

class Cliente:
    """
    Clase que representa a un cliente del gimnasio.

    Atributos:
        __id (int): Identificador único del cliente.
        __nombre (str): Nombre del cliente.
        __apellido (str): Apellido del cliente.
        __membresia (int): Número de membresía del cliente.
    """

    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        """
        Inicializa un nuevo objeto Cliente.

        Args:
            id (int, opcional): Identificador del cliente.
            nombre (str, opcional): Nombre del cliente.
            apellido (str, opcional): Apellido del cliente.
            membresia (int, opcional): Número de membresía.
        """
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__membresia = membresia

    @property
    def id(self):
        """int: Obtiene o establece el ID del cliente."""
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        """str: Obtiene o establece el nombre del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        """str: Obtiene o establece el apellido del cliente."""
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def membresia(self):
        """int: Obtiene o establece el número de membresía del cliente."""
        return self.__membresia

    @membresia.setter
    def membresia(self, membresia):
        self.__membresia = membresia

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Cliente.

        Returns:
            str: Representación legible del cliente.
        """
        return (f'ID: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}. Membresia: {self.membresia}')