"""
Sistema de Gestión de Biblioteca Universitaria
Punto de entrada del sistema
Desarrollado por: Henry Pazmiño (Líder / Integrador)
Grupo #1 — Programación 2 — UAE
"""

from src.gui.app import BibliotecaApp


def main():
    app = BibliotecaApp()
    app.run()


if __name__ == "__main__":
    main()
