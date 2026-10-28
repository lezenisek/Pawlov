# CNN Model, was die Daten verarbeitet

import torch
import torch.nn as nn  # neuronales Netz von PyTorch


#------------------- CNN Model -------------------

class PawlovCNN(nn.Module): # PawlovCNN ist also ein neuronales Netz von PyTorch 

    def __init__(self):   # ausführen, wenn das Modell erstellt wird
        super().__init__()

#--------------------- Merkmale (features) erkennen ---------------------

        self.features = nn.Sequential(   #Schritte nacheinander ausführen, um Merkmale zu erkennen

            # 1. Faltung (convolution)
            nn.Conv2d(
                in_channels=3, #drei Kanäle für RGB-Bilder
                out_channels=16, # 16 Filter --> 16 Merkmale werden erkannt
                kernel_size=3, # jeder Filter ist 3x3 Pixel groß
                padding=1 # damit die Größe des Bildes gleich bleibt, wird 1 Pixel gepaddet
            ),
            nn.ReLU(),
            nn.MaxPool2d(2),

            # 2. Faltung
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(2),

            # 3. Faltung
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )


        # --------------------------------------------------
        # KLASSIFIKATION
        # --------------------------------------------------

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(
                64 * 28 * 28,
                128
            ),

            nn.ReLU(),

            # Zwei mögliche Ergebnisse:
            # 0 = kein Männchen
            # 1 = Männchen
            nn.Linear(
                128,
                2
            )
        )


    # --------------------------------------------------
    # BILD DURCH DAS CNN SCHICKEN
    # --------------------------------------------------

    def forward(self, x):

        x = self.features(x)

        x = self.classifier(x)

        return x