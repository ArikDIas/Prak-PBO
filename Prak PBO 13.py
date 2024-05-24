from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class CustomWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Masukkan detail Anda:")
        self.layout.addWidget(self.label)

        self.entry_name = QLineEdit()
        self.entry_name.setPlaceholderText("Nama")
        self.layout.addWidget(self.entry_name)

        self.entry_nim = QLineEdit()
        self.entry_nim.setPlaceholderText("NIM")
        self.layout.addWidget(self.entry_nim)

        self.entry_hobby = QLineEdit()
        self.entry_hobby.setPlaceholderText("Hobi")
        self.layout.addWidget(self.entry_hobby)

        self.submit_button = QPushButton("Kirim")
        self.submit_button.setStyleSheet("background-color: #82E0AA")
        self.submit_button.clicked.connect(self.submit)
        self.layout.addWidget(self.submit_button)

        self.output_label = QLabel("")
        self.layout.addWidget(self.output_label)

        self.setLayout(self.layout)

    def submit(self):
        name = self.entry_name.text()
        nim = self.entry_nim.text()
        hobby = self.entry_hobby.text()

        details = f"Nama: {name}, NIM: {nim}, Hobi: {hobby}"
        self.label.setText(details)
        self.output_label.setText("")

if __name__ == "__main__":
    app = QApplication([])

    window = CustomWidgets()
    window.show()

    app.exec()