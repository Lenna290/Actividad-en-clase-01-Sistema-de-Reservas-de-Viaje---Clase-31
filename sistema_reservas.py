# Lista global que almacenará los usuarios registrados
Usuarios = []

def menu():
    """
    Esta función muestra el menú principal del sistema.
    Permite al usuario seleccionar entre diferentes opciones.
    """
    print("\nBienvenido al Sistema de Viajes")
    print("1. Registrar nuevo Usuario")
    print("2. Mostrar Viajes reservados")
    print("3. Actualizar información de un Usuario")
    print("4. Cancelar una reserva")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_Usuarios():
    """
    Esta función permite registrar un nuevo Usuario en el sistema.
    Pide al usuario ingresar el nombre y la edad del estudiante, y lo añade a la lista global 'usuarios'.
    """
    nombre = input("Ingresa el nombre del Usuario: ")
    Usuarios.append(nombre)
    print(f"Usuario {nombre} registrado con éxito.")
    
def mostrar_Usuarios():
    """
    Esta función muestra la lista de estudiantes registrados.
    Si no hay estudiantes registrados, informa al usuario.
    """
    if len(Usuarios) == 0:
        print("No hay Usuarios registrados.")
    else:
        print("Lista de Usuarios registrados:")
        for i, Usuario in enumerate(Usuarios, start=1):
            print(f"{i}. Nombre: {Usuario['nombre']}, Edad: {Usuario['edad']}")
            
def actualizar_Usuarios():
    """
    Esta función permite actualizar la información de un estudiante existente.
    Muestra una lista numerada de estudiantes para que el usuario seleccione a quién actualizar.
    """
    mostrar_Usuarios()
    if len(Usuarios) == 0:
        return
    
    try:
        seleccion = int(input("Selecciona el número del estudiante que deseas actualizar: ")) - 1
        if 0 <= seleccion < len(Usuarios):
            estudiante = Usuarios[seleccion]
            print(f"Usuario seleccionado: Nombre: {Usuarios['nombre']}, Edad: {Usuarios['edad']}")
            
            nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter para no cambiarlo): ")
            
            # Solo actualizamos si el usuario ingresó nuevos valores
            if nuevo_nombre:
                Usuarios['nombre'] = nuevo_nombre
            print(f"Usuario actualizado con éxito.")
        else:
            print("Usuario de estudiante no válido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        
def eliminar_Usuarios():
    """
    Esta función permite eliminar a un estudiante del sistema.
    Muestra una lista numerada de estudiantes para que el usuario seleccione a quién eliminar.
    """
    mostrar_Usuarios()
    if len(Usuarios) == 0:
        return
    
    try:
        seleccion = int(input("Selecciona el número del Usuario que deseas eliminar: ")) - 1
        if 0 <= seleccion < len(Usuarios):
            estudiante = Usuarios.pop(seleccion)
            print(f"Estudiante {Usuarios['nombre']} eliminado con éxito.")
        else:
            print("Número de Usuario no válido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        
def main():
    """
    Función principal que controla el flujo del programa.
    Usa un bucle while para mostrar el menú y realizar las acciones según la elección del usuario.
    """
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_Usuarios()
        elif opcion == '2':
            mostrar_Usuarios()
        elif opcion == '3':
            actualizar_Usuarios()
        elif opcion == '4':
            eliminar_Usuarios()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutamos la función principal para iniciar el programa
main()
            