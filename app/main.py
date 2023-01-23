import asyncio
import pathlib
import tkinter as tk
from rnn import predict_Spam_RNN


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Email Classifier")
        self.geometry("512x256")
        self.resizable(True, True)

        self.create_widgets()

    def create_widgets(self):
        self.email_content_label = tk.Label(self, text="Email Content:", font=("Arial", 12), anchor="center")
        self.email_content_label.grid(row=0, column=0, pady=5)

        self.email_content_input = tk.Text(self, height=10, width=20)
        self.email_content_input.grid(row=1, column=0, sticky="nsew")

        self.submit_button = tk.Button(self, text="Submit", state=tk.DISABLED, command=self.predict)
        self.submit_button.grid(row=2, columnspan=2, pady=10,sticky="nsew")

        self.output_label = tk.Label(self, text="", font=("Arial", 12), anchor="center")
        self.output_label.grid(row=3, columnspan=1, pady=10)

        self.columnconfigure(0, weight=1)

        self.email_content_input.bind("<Key>", self.enable_submit)

    def enable_submit(self, event):
        if self.email_content_input.get("1.0", tk.END).strip() != "":
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.submit_button.config(state=tk.DISABLED)

    def predict(self):
        text1 = self.email_content_input.get("1.0", tk.END)
        # Hier kann der Code für die Verarbeitung der Texte eingefügt werden
        print(text1)
        prediction = asyncio.run(predict_Spam_RNN(text1, pathlib.Path.cwd()))
        result = f'''The given text is with {round(prediction, 2)}% a Spam Mail'''
        self.output_label.config(text="The given text is with {:.2f}% a Spam Mail".format(prediction))


if __name__ == "__main__":
    app = App()
    app.mainloop()
