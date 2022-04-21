import sys
import traceback
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6 import uic, QtCore
from PyQt6.QtGui import QIcon
import json

from filemanagement import load_file


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowTitle("Texture Variables")
        self.setWindowIcon(QIcon('ui_images/appicon.ico'))
        self.setFixedSize(self.size())

        with open( "settings.json", "r" ) as f:
            json_filepath = json.loads(f.read())
        self.filepath = json_filepath["filepath"]
        self.textureVariables = []
        if self.filepath != "":
            with open(self.filepath, "r") as f:
                self.textureVariables = json.loads(f.read())

        self.data = [
                        {
                        "var": self.varNameLe_1,
                        "tex": self.texNameLe_1,
                        "rmv": self.removeBtn_1,
                        },
                        {
                        "var": self.varNameLe_2,
                        "tex": self.texNameLe_2,
                        "rmv": self.removeBtn_2,
                        },
                        {
                        "var": self.varNameLe_3,
                        "tex": self.texNameLe_3,
                        "rmv": self.removeBtn_3,
                        },
                        {
                        "var": self.varNameLe_4,
                        "tex": self.texNameLe_4,
                        "rmv": self.removeBtn_4,
                        },
                        {
                        "var": self.varNameLe_5,
                        "tex": self.texNameLe_5,
                        "rmv": self.removeBtn_5,
                        },
                        {
                        "var": self.varNameLe_6,
                        "tex": self.texNameLe_6,
                        "rmv": self.removeBtn_6,
                        },
                        {
                        "var": self.varNameLe_7,
                        "tex": self.texNameLe_7,
                        "rmv": self.removeBtn_7,
                        },
                        {
                        "var": self.varNameLe_8,
                        "tex": self.texNameLe_8,
                        "rmv": self.removeBtn_8,
                        },
                        {
                        "var": self.varNameLe_9,
                        "tex": self.texNameLe_9,
                        "rmv": self.removeBtn_9,
                        },
                    ]

        with open("cssfiles/removestyle.css", "r") as f:
            removeStyle = f.read()

        for elem in self.data:
            elem["rmv"].setStyleSheet(removeStyle)

        self.rerenderList()

        self.filepathBtn.clicked.connect(lambda: load_file( self ))

        self.varName = ""
        self.texName = ""

        self.varNameLe.textChanged.connect(lambda: self.setVarName(self.varNameLe.text()))
        self.texNameLe.textChanged.connect(lambda: self.setTexName(self.texNameLe.text()))

        self.addBtn.clicked.connect(lambda: self.addNewItem(self.varName, self.texName))

        self.saveBtn.clicked.connect(self.saveFile)

    def createItem( self, index, texture_variable ):
        var, tex, rmv = self.data[index].values()
        var.setEnabled(True)
        tex.setEnabled(True)
        rmv.setEnabled(True)
        var.setText(texture_variable["var"])
        tex.setText(texture_variable["tex"])
        rmv.setText("remove")
        rmv.clicked.connect(lambda: self.removeItem(index))

    def removeItem( self, index ):
        try:
            self.textureVariables.pop(index)
            self.rerenderList()
        except Exception:
            print(traceback.format_exc())

    def rerenderList( self ):
        # Clear List
        for elem in self.data:
            for item in elem.values():
                item.setEnabled(False)
            elem["rmv"].setText("")
            # We only want to connect one signal
            try:
                elem["rmv"].clicked.disconnect()
            except Exception:
                pass

        # Rerender
        for index, texture_variable in enumerate(self.textureVariables):
            self.createItem( index, texture_variable )

    def addNewItem( self, var, tex ):
        try:
            elem = { "var": var, "tex": tex }
            self.textureVariables.append(elem)
            self.rerenderList()
            self.varName = ""
            self.texName = ""
            self.varNameLe.setText = ""
            self.texNameLe.setText = ""
        except Exception:
            print(traceback.format_exc())

    def setVarName( self, text ):
        self.varName = text

    def setTexName( self, text ):
        self.texName = text

    def saveFile( self ):
        with open(self.filepath, "w") as f:
            json_file = json.dumps(self.textureVariables, indent=2)
            f.write(json_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet(open('cssfiles/stylesheet.css').read())

    window = MyApp()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print(' Closing Window ... ')
