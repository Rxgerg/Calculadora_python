# 🧮 Calculadora de Escritorio en Python

Calculadora de escritorio desarrollada en Python que permite realizar operaciones matemáticas **básicas y avanzadas** desde la terminal. Además, cuenta con un **historial persistente** de operaciones que se guarda automáticamente en un archivo de texto, y puede ser consultado o eliminado en cualquier momento.

---

## ✨ Características

- ✅ **Operaciones básicas:** suma, resta, multiplicación y división.  
- ✅ **Operaciones avanzadas:** potencia, raíz cuadrada, módulo y factorial.  
- ✅ **Historial persistente:** cada operación se almacena automáticamente en un archivo de texto.  
- ✅ **Gestión del historial:** opción para consultar o borrar el historial desde el menú.  
- ✅ **Validaciones robustas:** manejo de errores como:
  - División entre cero.
  - Raíz cuadrada de números negativos.
  - Factorial de números no enteros o negativos.
- ✅ **Código modular:** estructura clara separada por funcionalidades.

---

## 🗂️ Estructura del Proyecto

```plaintext
calculadora/
│
├── main.py           # Punto de entrada, menú principal
├── operations.py     # Funciones matemáticas
├── history.py        # Manejo del historial (en memoria y archivo)
└── Functions/
    └── utils.py      # Funciones auxiliares (validación, menús, entradas)
```

---

## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Rxgerg/Calculadora_python.git
cd develop
```

2. Asegúrate de tener Python 3.x instalado.
- 💡 Este proyecto no requiere librerías externas para su versión de consola.

---

## ▶️ Ejecución
Desde la terminal, ejecuta el archivo principal:
```bash
python main.py
```

---
## 💡 Uso
Al iniciar la aplicación, se muestra un menú interactivo con opciones para:

-   Realizar operaciones matemáticas.

-   Consultar o borrar el historial de operaciones.

-   Salir de la aplicación.

Solo sigue las instrucciones en pantalla para introducir los números y seleccionar la operación deseada.

---

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.