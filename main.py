"""
Sistema de Gestión de Biblioteca Universitaria
Punto de entrada del sistema
"""

from src.gui.app import BibliotecaApp


def main():
    app = BibliotecaApp()
    app.run()


if __name__ == "__main__":
    main()
