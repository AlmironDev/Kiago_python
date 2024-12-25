from View.UsuarioView import UsuarioView

print(" \n")
"""
Creacion de un nuevo usuario a la empresa Kiago
"""


UsuarioView = UsuarioView()
UsuarioView.create_user(
    nombre=414, rol=555, phone="s5555", categoria="Desarrollo"
)
valor_carlos = UsuarioView.create_user(123, 123, "123456789", "Psicologia")

print("valor_carlos", valor_carlos  )
print(UsuarioView.get_users())
print(UsuarioView.get_user(valor_carlos['_id']))
print(
    UsuarioView.update_user(
        {
            "_id": valor_carlos["_id"],
            "nombre": "Carlos_2",
            "rol": "Profesor",
            "phone": "123456789",
            "categoria": "Psicologia",
        }
    )
)

print(UsuarioView.get_users())


print(" \n")
