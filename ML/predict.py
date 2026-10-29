# Klassen vorhersagen anhand der Merkmale, die das Modell extrahiert hat

import torch

from PIL import Image # Pillow zum Öffnen von Bildern
from torchvision import transforms

from model import PawlovCNN

#------------------- Datenvorverarbeitung -------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),# immer gleiche Bildgröße 
    transforms.ToTensor() # Tensor für PyTorch erstellen
])


#------------------- Modell laden -------------------

model = PawlovCNN() 

model.load_state_dict( # aktuellen Trainingsstand laden 
    torch.load(
        "katze_sitz_model.pth",
        map_location=torch.device("cpu") # Modell so laden, dass es auf der CPU läuft, auch wenn es auf einer GPU trainiert wurde
        
    )
)

model.eval() # Modell soll nicht mehr lernen, sondern nur Vorhersagen machen


#------------------- Klassen -------------------

classes = [
    "katze_sitz",
    "kein_katze_sitz"
]


#------------------ Vorhersagefunktion -------------------

def predict(image_path):

    # Bild öffnen
    image = Image.open(image_path).convert("RGB")

    # Bild vorbereiten
    image = transform(image)

    # Zusätzliche Dimension für Batch hinzufügen
    image = image.unsqueeze(0)


    #------------------- Vorhersage -------------------

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(output, dim=1)

        probability, predicted_class = torch.max( # Wahrscheinlichkeit und Klasse mit der höchsten Wahrscheinlichkeit auswählen
            probabilities, 
            1
        )


    #------------------- Ergebnis anzeigen -------------------

    class_name = classes[predicted_class.item()]

    percentage = probability.item() * 100

    print("Erkannte Klasse:", class_name)
    print(f"Wahrscheinlichkeit: {percentage:.2f}%")

    return class_name, percentage


#------------------- Beispielaufruf -------------------


# Schnittstelle mit Logik: Hier muss ein Bild übergeben werden, das vom Laptop aufgenommen wurde. Das Bild wird dann an die Funktion predict() übergeben, die die Vorhersage durchführt und das Ergebnis zurückgibt.
predict("testbild.jpg") # Hier würde dann das vom Laptop aufgenommene Bild übergeben werden 
