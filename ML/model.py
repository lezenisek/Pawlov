# CNN Model, was die Daten verarbeitet

import torch
import torch.nn as nn  # neuronales Netz von PyTorch


#------------------- CNN Model -------------------

class PawlovCNN(nn.Module): # PawlovCNN ist also ein neuronales Netz von PyTorch 

    def __init__(self):   # ausführen, wenn das Modell erstellt wird
        super().__init__()

#--------------------- Merkmale (features) erkennen ---------------------

        self.features = nn.Sequential(   #Schritte nacheinander ausführen, um Merkmale zu erkennen

            # Bildgröße: 224x224 Pixel, 3 Kanäle (RGB)

            # 1. Faltung (convolution)
            nn.Conv2d(
                in_channels=3, #drei Kanäle für RGB-Bilder
                out_channels=16, # 16 Filter --> 16 Merkmale werden erkannt
                kernel_size=3, # jeder Filter ist 3x3 Pixel groß
                padding=1 # damit die Größe des Bildes gleich bleibt, wird 1 Pixel gepaddet
            ),
            nn.ReLU(), # pos Werte behalten, neg Werte auf 0 setzen
            nn.MaxPool2d(2), # reduziert die Größe des Bildes um die Hälfte (Pooling)
                            # z.B. 224x224 --> 112x112
            # 2. Faltung
            nn.Conv2d(
                in_channels=16, # 16 Merkmalskarten von der vorherigen Faltung
                out_channels=32, # 32 Merkmalskarten werden erzeugt
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(2), # Bildgröße: 112x112 --> 56x56

            # 3. Faltung
            nn.Conv2d(
                in_channels=32, # 32 Merkmalskarten von der vorherigen Faltung
                out_channels=64, # 64 Merkmalskarten werden erzeugt
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(2) # Bildgröße: 56x56 --> 28x28
        )


#--------------------- Klassifizierung ---------------------

        self.classifier = nn.Sequential( #classifier ist ein neuronales Netz von PyTorch, das die Merkmale klassifiziert

            nn.Flatten(), #Merkmalsmatrizen in einen Vektor umwandeln, damit sie in den Klassifikator eingespeist werden können

            nn.Linear(
                64 * 28 * 28, # 64 Merkmalskarten, jede 28x28 Pixel groß
                128 # auf 128 Merkmale reduzieren, um die Klassifizierung zu erleichtern
                # 128 = Hyperparameter, kann angepasst werden, um die Leistung des Modells zu verbessern
            ),

            nn.ReLU(),

            # Zwei mögliche Ergebnisse:
            # "Klasse" 0 = kein Männchen
            # "Klasse" 1 = Männchen
            nn.Linear(
                128,
                2 # 2 Klassen, die das Modell vorhersagen kann
            )
        )


#--------------------- Vorwärtsdurchlauf ---------------------

    def forward(self, x): # x = Eingabebild, das durch das Modell läuft

        x = self.features(x) # Merkmale werden erkannt

        x = self.classifier(x) # Ausgabe wird klassifiziert

        return x # Ausgabe des Modells (z.B. Wahrscheinlichkeit, dass das Bild ein Männchen zeigt)