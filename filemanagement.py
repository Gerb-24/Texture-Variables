from PyQt6.QtWidgets import QFileDialog
import ast
import os
import json

def load_file(self):
    filepath, _ = QFileDialog.getOpenFileName(self, "Load File", "", "JSON(*.json)")
    if filepath == "":
        return
    else:
        self.filepath = filepath
        save_filepath( filepath )
        with open(self.filepath, "r") as f:
            self.textureVariables = json.loads(f.read())
        self.rerenderList()

def save_filepath( filepath ):
    save_data = {
    "filepath": filepath
    }
    json_data = json.dumps( save_data, indent=2 )
    with open("settings.json", "w") as f:
        f.write(json_data)
