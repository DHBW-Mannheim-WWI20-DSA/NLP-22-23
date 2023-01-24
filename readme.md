# NLP- Email-Spam Klassifikation 

### Datensatz ohne Metadaten: https://www.kaggle.com/datasets/adarshkumarjha/email-spam-detection-sentiment-analysis
### Datensatz mit Metadaten: https://www.kaggle.com/datasets/veleon/ham-and-spam-dataset?datasetId=107917&sortBy=voteCount

Dieses Notebook enthält die gesamten Dateien der Zusammenarbeit von Tobias Kister (Martriklnr. 9416513), Daniel Schmitz (Martriklnr. 6695185) und Amina Uicker-Darwish (Martrikelnr. 8278962)

Endergebnisse: 
- Das Repository enthält drei Ordner (RNN -> Daniel, Spacy-> Amina, Transformer-> Tobi) die jeweils die Notebooks der trainierten Modelle enthalten. Für die Ausführung müssen nur die in den Dateien importierten Bibiliotheken installiert werden sowie die genutzten Datensätze heruntergeladen werden
- Die Modelle wurden jeweils auf Basis der Accuracy, Recall und Precision evaluiert
- Im Ordner "Application" befinden sich die Dateien für ein Frontend, in dem die trainierten Modelle getestet werden können. Für die Einschätzung einer Spam Mail, kann der Nutzer das Modell selbst wählen und entscheiden ob er/sie ledglich Text als Input gibt oder auch zusätzlich Metadaten 
- Im Ordner "App" befindet sich ein einfaches Frontend, dass das eines der besten Modelle (RNN) als Schätzer nutzt. Hier kann der/die Nutzer:in über die Eingabe des Texts einer Email eine prozentuale Einschätzung erhalten ob die Mail Spam ist oder nicht
