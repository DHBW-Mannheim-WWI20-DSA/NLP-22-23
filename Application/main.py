import sys
import pathlib
from typing import Union

from PyQt5.QtWidgets import QApplication, QComboBox, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QPlainTextEdit, QPushButton

from Application.transformer import predict_Spam_transformer


# Define Function to Build Path to Model
def build_model_folder_path(metadata_bool: bool, model_name: str) -> pathlib.Path:
    """
    Build Path to Model Folder
    :param metadata_bool: Boolean to Determine if Metadata is Used
    :param model_name: Name of Model
    :return: pathlib.Path: Path to Model Folder
    """
    # Get Root Path
    root_path = pathlib.Path.cwd()
    # Get Path to Model Folder
    model_folder_path = pathlib.Path.joinpath(root_path, 'models')
    # Decide if Metadata is used
    if metadata_bool:
        meta_folder_path = pathlib.Path.joinpath(model_folder_path, 'meta')
    else:
        meta_folder_path = pathlib.Path.joinpath(model_folder_path, 'text')
    return pathlib.Path.joinpath(meta_folder_path, model_name)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Email Classificator")

        # Set Input of the App
        # Metadata used ?
        self.metadata_label = QLabel("Should Metadata be used:")
        self.metadata_input = QComboBox()
        self.metadata_input.addItems(["", "No", "Yes"])
        self.metadata_input.currentTextChanged.connect(self.metadata_changed)

        # What Type of Model should be used ?
        self.model_type_label = QLabel("Model used:")
        self.model_type_input = QComboBox()
        self.model_type_input.addItems(["", "NLTK", "RNN", "Spacy", "Transformer"])
        self.model_type_input.currentTextChanged.connect(self.model_changed)

        # Define Input Fields of the App
        # Metadata
        self.metadata_txt_label = QLabel("Metadata:")
        self.metadata_txt_label.setVisible(False)
        self.metadata_txt_input = QPlainTextEdit()
        self.metadata_txt_input.setPlaceholderText("Enter Metadata here ...")
        self.metadata_txt_input.setVisible(False)  # Hide it at the beginning
        self.metadata_txt_input.textChanged.connect(self.update_analyse_button)

        # Email Message
        self.email_message_label = QLabel("Email Message:")
        self.email_message_label.setVisible(False)
        self.email_message_input = QPlainTextEdit()
        self.email_message_input.setPlaceholderText("Enter Email Message here ...")
        self.email_message_input.setVisible(False)  # Hide it at the beginning
        self.email_message_input.textChanged.connect(self.update_analyse_button)

        # Analyse Button
        self.analyse_button = QPushButton("Analyse")
        self.analyse_button.setEnabled(False)  # Disable it at the beginning
        self.analyse_button.clicked.connect(self.analyse_button_clicked)

        # Output of the Analyse
        self.output_label = QLabel("Output:")
        self.output_input = QLineEdit()
        self.output_input.setPlaceholderText("Output will be displayed here ...")
        self.output_input.setReadOnly(True)
        output_layout = QVBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_input)

        # Define Layout of the Application
        layout = QFormLayout()
        layout.addRow(self.metadata_label, self.metadata_input)
        layout.addRow(self.model_type_label, self.model_type_input)
        layout.addRow(self.metadata_txt_label, self.metadata_txt_input)
        layout.addRow(self.email_message_label, self.email_message_input)
        layout.addRow(self.analyse_button)
        layout.addRow(output_layout)

        # Set Layout of the Application
        self.setLayout(layout)

    # What happens when Metadata is changed ?
    def metadata_changed(self, text):
        print("Metadata changed to: " + text)
        if text == "Yes":
            self.metadata_txt_input.setVisible(True)
            self.metadata_txt_label.setVisible(True)
            self.email_message_input.setVisible(True)
            self.email_message_label.setVisible(True)
        else:
            self.metadata_txt_input.setVisible(False)
            self.metadata_txt_label.setVisible(False)
            self.email_message_input.setVisible(True)
            self.email_message_label.setVisible(True)
        self.update_analyse_button()

    # What happens when Model is changed ?
    def model_changed(self, text):
        print("Model changed to: " + text)

    # What happens when Input Fields are changed ?
    def update_analyse_button(self):
        if self.metadata_input.currentText() == "Yes":
            if self.metadata_txt_input.toPlainText() != "" and self.email_message_input.toPlainText() != "":
                self.analyse_button.setEnabled(True)
            else:
                self.analyse_button.setEnabled(False)
        else:
            if self.email_message_input.toPlainText() != "":
                self.analyse_button.setEnabled(True)
            else:
                self.analyse_button.setEnabled(False)

    # What happens when Analyse Button is clicked ?
    def analyse_button_clicked(self):
        # Get Inputs
        model_type: Union[str, None] = self.model_type_input.currentText()
        metadata_used: Union[bool, None] = True if self.metadata_input.currentText() == "Yes" else False
        email_content: Union[str, None] = None
        metadata_content: Union[str, None] = None
        if self.metadata_input.currentText() == "Yes":
            email_content = self.email_message_input.toPlainText()
        if self.email_message_input.toPlainText() != "":
            metadata_content = self.email_message_input.toPlainText()

        # Analyse
        print("Model: " + model_type)
        print("Metadata used: " + str(metadata_used))
        print("Email Content: " + str(email_content))
        print("Metadata Content: " + str(metadata_content))

        if model_type == "NLTK":
            # Do something
            pass
        elif model_type == "RNN":
            # Do something
            pass
        elif model_type == "Spacy":
            # Do something
            pass
        elif model_type == "Transformer":
            # Do something
            predict_Spam_transformer(
                email_content=email_content,
                metadata_content=metadata_content,
                path_to_model=build_model_folder_path(metadata_bool=metadata_used, model_name=model_type),
                metadata_used=metadata_used
            )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # main()
    print(build_model_folder_path(True, "Transformer"))
