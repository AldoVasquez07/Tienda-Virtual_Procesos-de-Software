import pyodbc


def aspectos_bd():
    with open("../ambiente/configuracion.txt", "r") as aspectos:
        return [line.strip() for line in aspectos.readlines() if line.strip()]


def conexion():
    lista_conexion = aspectos_bd()
    try:
        con = pyodbc.connect(
            f'Driver={lista_conexion[0]};'
            f'SERVER={lista_conexion[1]};'
            f'DATABASE={lista_conexion[2]};'
            f'Trusted_Connection={lista_conexion[3]}'
        )
        return con

    except Exception as e:
        print(f'Error en la conexión: {str(e)}')
        return None
