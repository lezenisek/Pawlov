from pico import Raspy
from logic import RewardSystem

# ============================================================
# INTERAKTIVES TESTPROGRAMM
# ============================================================
def main():
    spender = None
    try:
        # 1. Pico verbinden
        spender = Raspy()

        # 2. Belohnungssystem starten
        belohnung = RewardSystem(spender=spender)

        print("\n" + "=" * 40)
        print("PAWLOV TESTKONSOLE")
        print("  ENTER      = Belohnung auslösen (Ton + Motor)")
        print("  u + ENTER  = Neuen Sound (MP3/WAV) laden")
        print("  q + ENTER  = Beenden")
        print("=" * 40)

        while True:
            befehl = input("\nEingabe: ").strip()

            if befehl == "":
                belohnung.success()

            elif befehl.lower() == "u":
                pfad = input("Vollständigen Pfad zur MP3/WAV-Datei eingeben: ").strip(' "\'')
                try:
                    belohnung.sound_hochladen(pfad)
                    # Testweise anspielen
                    belohnung.klingel()
                except Exception as e:
                    print("Fehler beim Hochladen:", e)

            elif befehl.lower() == "q":
                print("Programm beendet.")
                break

    finally:
        if spender:
            spender.schliessen()

if __name__ == "__main__":
    main()