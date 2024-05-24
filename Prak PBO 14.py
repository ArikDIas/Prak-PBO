from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

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

        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("background-color: #E9F5AA")
        self.reset_button.clicked.connect(self.reset)
        self.layout.addWidget(self.reset_button)

        self.output_label = QLabel("")
        self.layout.addWidget(self.output_label)

        self.setLayout(self.layout)

    def submit(self):
        name = self.entry_name.text().strip()
        nim = self.entry_nim.text().strip()
        hobby = self.entry_hobby.text().strip()

        if not name:
            QMessageBox.critical(self, "Kesalahan", "Nama belum diisi!")
            return
        if not nim:
            QMessageBox.critical(self, "Kesalahan", "NIM belum diisi!")
            return
        if not nim.isdigit():
            QMessageBox.critical(self, "Kesalahan", "NIM harus berupa angka!")
            return
        if not hobby:
            QMessageBox.critical(self, "Kesalahan", "Hobi belum diisi!")
            return

        details = f"Nama: {name}, NIM: {nim}, Hobi: {hobby}"
        self.label.setText(details)
        self.output_label.setText("")

    def reset(self):
        self.entry_name.clear()
        self.entry_nim.clear()
        self.entry_hobby.clear()
        self.label.setText("Masukkan detail Anda:")
        self.output_label.setText("")

if __name__ == "__main__":
    app = QApplication([])

    window = CustomWidgets()
    window.show()

    app.exec()
