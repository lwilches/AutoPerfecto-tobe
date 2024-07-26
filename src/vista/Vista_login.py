from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Vista de Login de  usuario

class LoginWindow(QDialog):
    def __init__(self, logica):
        super().__init__()
        self.logica = logica
        self.setWindowTitle('Login')
        self.setFixedSize(400, 150)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))

        self.inicializar_GUI()

    def inicializar_GUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 30, 0, 0)  # Agrega márgenes

        # Layouts para cada fila
        fila_usuario = QHBoxLayout()
        fila_contrasena = QHBoxLayout()

        self.etiqueta_usuario = QLabel('Usuario')
        self.etiqueta_usuario.setFixedWidth(60)  # Ancho fijo para la etiqueta
        self.campo_usuario = QLineEdit()
        self.campo_usuario.setFixedSize(180, 25)
        fila_usuario.addStretch()  # Espaciador a la izquierda
        fila_usuario.addWidget(self.etiqueta_usuario)
        fila_usuario.addWidget(self.campo_usuario)
        fila_usuario.addStretch()  # Espaciador a la derecha

        self.etiqueta_contrasena = QLabel('Contraseña')
        self.etiqueta_contrasena.setFixedWidth(60)  # Ancho fijo para la etiqueta
        self.campo_contrasena = QLineEdit()
        self.campo_contrasena.setEchoMode(QLineEdit.Password)
        self.campo_contrasena.setFixedSize(180, 25)
        fila_contrasena.addStretch()  # Espaciador a la izquierda
        fila_contrasena.addWidget(self.etiqueta_contrasena)
        fila_contrasena.addWidget(self.campo_contrasena)
        fila_contrasena.addStretch()  # Espaciador a la derecha

        self.boton_login = QPushButton('Login')
        self.boton_login.setFixedSize(80, 30)
        self.boton_login.clicked.connect(self.verificar_credenciales)

        # Layout principal
        layout.addLayout(fila_usuario)
        layout.addLayout(fila_contrasena)
        layout.addWidget(self.boton_login, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        print('GUI inicializada')

    def verificar_credenciales(self):
        
        usuario = self.campo_usuario.text()
        contrasena = self.campo_contrasena.text()

        # Validación de usuario
        usuario_valido = self.logica.autenticar_usuario(usuario, contrasena)
        if usuario_valido:
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Usuario o contraseña incorrectos')
   

       