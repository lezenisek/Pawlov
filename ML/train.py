# Hier wird das Modell trainiert und gespeichert
import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from model import PawlovCNN


#------------------- Trainingseinstellungen -------------------

BATCH_SIZE = 16 # Größe der Datenmenge, die gleichzeitig durch das Modell geschickt wird
EPOCHS = 20 # Anzahl der Durchläufe durch den gesamten Trainingsdatensatz
LEARNING_RATE = 0.001  # Lernrate, wie stark die Gewichte des Modells bei jedem Schritt angepasst werden


#------------------- Datenvorverarbeitung -------------------

transform = transforms.Compose([ 
    transforms.Resize((224, 224)), # Alle Bilder gleiche Größe von 224x224 Pixeln
    transforms.ToTensor() # in Tensor umwandeln, damit PyTorch sie verarbeiten kann
])


#------------------- DATENSÄTZE LADEN -------------------

train_dataset = datasets.ImageFolder(
    "dataset/train", # Pfad zum Trainingsdatensatz
    transform=transform
)

validation_dataset = datasets.ImageFolder(
    "dataset/validation", # Pfad zum Validierungsdatensatz
    transform=transform
)


#------------------- DATALOADER -------------------

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)


#------------------- MODELL ERSTELLEN -------------------

model = PawlovCNN()


#------------------- FEHLERFUNKTION -------------------

criterion = nn.CrossEntropyLoss()


#------------------- OPTIMIZER -------------------

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)


# --------------------------------------------------
# TRAINING
# --------------------------------------------------

for epoch in range(EPOCHS):

    model.train()

    training_loss = 0

    for images, labels in train_loader:

        # Alte Berechnungen zurücksetzen
        optimizer.zero_grad()

        # Bilder durch das CNN schicken
        outputs = model(images)

        # Fehler berechnen
        loss = criterion(outputs, labels)

        # Berechnen, was verändert werden muss
        loss.backward()

        # Modell verbessern
        optimizer.step()

        training_loss += loss.item()


    # --------------------------------------------------
    # VALIDIERUNG
    # --------------------------------------------------

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in validation_loader:

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)

            correct += (predicted == labels).sum().item()


    accuracy = 100 * correct / total

    print(
        f"Epoche {epoch + 1}/{EPOCHS} | "
        f"Loss: {training_loss:.2f} | "
        f"Validation Accuracy: {accuracy:.2f}%"
    )


# --------------------------------------------------
# MODELL SPEICHERN
# --------------------------------------------------

torch.save(
    model.state_dict(),
    "maennchen_model.pth"
)

print("Training abgeschlossen.")
print("Modell wurde gespeichert.")