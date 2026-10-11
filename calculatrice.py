import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        self.expression = ""
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Calculatrice")
        self.setFixedSize(320, 480)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
            }
            QLineEdit {
                background-color: #2a2a3c;
                color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton {
                background-color: #3a3a4c;
                color: #ffffff;
                border: none;
                border-radius: 10px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #4a4a5c;
            }
            QPushButton:pressed {
                background-color: #55557a;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)

        # Écran d'affichage
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(70)
        self.display.setFont(QFont("Arial", 28))
        layout.addWidget(self.display)

        # Grille des boutons
        grid = QGridLayout()
        grid.setSpacing(8)

        boutons = [
            ("C", 0, 0, "#e74c3c"), ("⌫", 0, 1, "#3a3a4c"), ("%", 0, 2, "#3a3a4c"), ("/", 0, 3, "#e67e22"),
            ("7", 1, 0, None), ("8", 1, 1, None), ("9", 1, 2, None), ("*", 1, 3, "#e67e22"),
            ("4", 2, 0, None), ("5", 2, 1, None), ("6", 2, 2, None), ("-", 2, 3, "#e67e22"),
            ("1", 3, 0, None), ("2", 3, 1, None), ("3", 3, 2, None), ("+", 3, 3, "#e67e22"),
            ("0", 4, 0, None), (".", 4, 1, None), ("=", 4, 2, "#27ae60"), (None, 4, 3, None),
        ]

        for texte, ligne, colonne, couleur in boutons:
            if texte is None:
                continue
            btn = QPushButton(texte)
            btn.setFixedSize(65, 65)
            if couleur:
                btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {couleur};
                        color: white;
                        border-radius: 10px;
                        font-size: 18px;
                    }}
                    QPushButton:hover {{
                        background-color: {couleur}dd;
                    }}
                """)
            # "=" prend la place de deux colonnes visuellement
            if texte == "=":
                grid.addWidget(btn, ligne, colonne, 1, 2)
            else:
                grid.addWidget(btn, ligne, colonne)

            btn.clicked.connect(lambda checked, t=texte: self.gerer_clic(t))

        layout.addLayout(grid)
        self.setLayout(layout)

    def gerer_clic(self, texte):
        if self.expression == "Erreur" and texte != "C":
            self.expression = ""

        if texte == "C":
            self.expression = ""
        elif texte == "⌫":
            self.expression = self.expression[:-1]
        elif texte == "=":
            try:
                # Remplacement pour compatibilité affichage/calcul
                resultat = str(eval(self.expression.replace("%", "/100")))
                self.expression = resultat
            except Exception:
                self.expression = "Erreur"
        else:
            self.expression += texte

        self.display.setText(self.expression)


def main():
    app = QApplication(sys.argv)
    fenetre = Calculatrice()
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
