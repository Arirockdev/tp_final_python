import sqlite3

def create_database():
    """Create the SQLite database and the products table if not exists."""
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )''')
    conn.commit()
    conn.close()

def agregar_producto():
    """Add a new product to the inventory."""
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio del producto: "))
    categoria = input("Categoría del producto: ")

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    conn.close()
    print("Producto agregado exitosamente.")

def mostrar_productos():
    """Display all products in the inventory."""
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()

    print("\nInventario:")
    print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
    print("-" * 50)
    for producto in productos:
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]:.2f} | {producto[5]}")

def actualizar_producto():
    """Update the quantity of a specific product by ID."""
    id_producto = int(input("ID del producto a actualizar: "))
    nueva_cantidad = int(input("Nueva cantidad: "))

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
    conn.commit()
    conn.close()
    print("Producto actualizado exitosamente.")

def eliminar_producto():
    """Delete a product from the inventory by ID."""
    id_producto = int(input("ID del producto a eliminar: "))

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    conn.close()
    print("Producto eliminado exitosamente.")

def buscar_producto():
    """Search for a product by ID."""
    id_producto = int(input("ID del producto a buscar: "))

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    conn.close()

    if producto:
        print("\nProducto encontrado:")
        print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
        print("-" * 50)
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]:.2f} | {producto[5]}")
    else:
        print("Producto no encontrado.")

def reporte_bajo_stock():
    """Generate a report of products with low stock."""
    limite = int(input("Ingrese el límite de cantidad para el reporte: "))

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    conn.close()

    print("\nReporte de Bajo Stock:")
    print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
    print("-" * 50)
    for producto in productos:
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]:.2f} | {producto[5]}")

def menu():
    """Display the main menu and handle user interaction."""
    while True:
        print("\nMenú Principal:")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de Bajo Stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    create_database()
    menu()
