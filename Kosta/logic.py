import sys
import shutil
import os
from pico import Raspy

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

# Plattformunabhängiges Sound-Handling
try:
    import winsound
except ImportError:
    winsound = None


class RewardSystem:

    ERLAUBTE_FORMATE = (".wav", ".mp3")


    def __init__(self, spender: Raspy, sound_file: str = None, sound_folder: str = "sounds"):
        self.spender = spender
        self.sound_folder = sound_folder
        self.aktuelle_sound_file = None

        # Ordner für die Sounds sicherstellen
        os.makedirs(self.sound_folder, exist_ok=True)

        pygame.mixer.init()

        if sound_file:
            self.load_file(sound_file)

    def upload_file(self, quell_pfad: str) -> str: 
        """
        Kopiert eine externe WAV- oder MP3-Datei in den Projekt-Soundordner
        und aktiviert sie als aktuellen Konditionierungston.
        """
        if not os.path.isfile(quell_pfad):
            raise FileNotFoundError(f"Die angegebene Datei existiert nicht: {quell_pfad}")

        dateiendung = os.path.splitext(quell_pfad)[1].lower()
        if dateiendung not in self.ERLAUBTE_FORMATE:
            raise ValueError(f"Ungültiges Dateiformat '{dateiendung}'. Erlaubt sind: {self.ERLAUBTE_FORMATE}")

        dateiname = os.path.basename(quell_pfad)
        ziel_pfad = os.path.join(self.sound_folder, dateiname)

        # Datei in den Soundordner kopieren
        shutil.copy(quell_pfad, ziel_pfad)
        print(f"[Audio] Sound '{dateiname}' erfolgreich hochgeladen/gespeichert.")

        # Sofort als aktive Datei setzen
        self.load_file(ziel_pfad)
        return ziel_pfad

    def load_sound(self, datei_pfad: str):
        """Setzt eine vorhandene Sound-Datei als aktiven Ton."""
        if not os.path.isfile(datei_pfad):
            raise FileNotFoundError(f"Sounddatei nicht gefunden: {datei_pfad}")
        self.aktuelle_sound_file = datei_pfad
        print(f"[Audio] Aktiver Sound gesetzt auf: {os.path.basename(datei_pfad)}")


    def klingel(self):
        """Spielt ein akustisches Signal ab (Windows: Ton, Linux/Mac: Bell-Zeichen)."""
        if not self.aktuelle_sound_datei:
            if winsound is not None:
                # Spielt den Windows-Hinweiston ab
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
                print("[Audio] Kein Sound hinterlegt – spiele Standard-Glocke.")
                print("\a", end="", flush=True)
                return
            else:
                    # Fallback für Raspberry Pi / Linux Terminal
                    sys.stdout.write("\a")
                    sys.stdout.flush()


        """Spielt die hinterlegte Audiodatei ab."""
        try:
            pygame.mixer.music.load(self.aktuelle_sound_datei)
            pygame.mixer.music.play()
        except Exception as fehler:
            print(f"[Audio-Fehler] Konnte Sound nicht abspielen: {fehler}")

    def success(self):
        """
        Klassische Pawlowsche Konditionierung:
        1. Akustisches Signal abspielen
        2. Leckerli über Motor ausgeben
        """
        print("\n--- ERFOLG: Katze hat Aufgabe ausgeführt! ---")
        
        # Erst Glocke/Ton
        self.klingel()
        
        # Dann Motor ansteuern
        self.spender.leckerli_ausgeben()

