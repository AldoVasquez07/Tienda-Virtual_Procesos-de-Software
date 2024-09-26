from modelos.conexion import conexion
from modelos.models import User


def gestor_login(correo, contrasena):
    login_query = "SELECT * FROM usuario WHERE correo = ? AND contrasena = ?"
    cursor = conexion().cursor()
    cursor.execute(login_query, (correo, contrasena))
    user = User(*cursor.fetchone())
    cursor.close()

    if user:
        return True, user
    else:
        return False, None


if __name__ == "__main__":
    gestor_login('avasquezl@ulasalle.edu.pe', '123456')
