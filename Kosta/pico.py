import serial
import serial.tools.list_ports
import time


# ============================================================
# PAWLOV LECKERLI-SPENDER
# ============================================================
#
# Dieses Programm sucht automatisch nach dem Raspberry Pi Pico
# des Pawlov-Leckerlispenders.
#
# Ein COM-Port muss NICHT manuell eingetragen werden.
#
# Das Programm fragt alle vorhandenen seriellen Anschlüsse:
#
#       BIST_DU_PAWLOV?
#
# Der Pawlov-Pico antwortet:
#
#       JA_PAWLOV
#
# Dadurch kann der richtige Pico automatisch gefunden werden.
# ============================================================
class Raspy:
    """Verwaltet die serielle Verbindung zum Raspberry Pi Pico des Pawlov-Leckerlispenders."""

    def __init__(self):
        self.pico = None
        self.verbinden()

    def verbinden(self):
        print("Suche Pawlov-Leckerlispender...")

        for port in serial.tools.list_ports.comports():
            print("Teste:", port.device)
            verbindung = None

            try:
                verbindung = serial.Serial(
                    port=port.device,
                    baudrate=115200,
                    timeout=2,
                    write_timeout=2
                )

                # Kurz warten, da manche Picos beim Öffnen der seriellen Schnittstelle neu starten
                time.sleep(1)
                verbindung.reset_input_buffer()

                print("  -> Sende Anfrage...")
                verbindung.write(b"BIST_DU_PAWLOV?\n")
                verbindung.flush()

                print("  -> Warte auf Antwort...")
                antwort = verbindung.readline().decode(errors="ignore").strip()
                print("  -> Antwort:", repr(antwort))

                if antwort == "JA_PAWLOV":
                    print("Pawlov-Leckerlispender gefunden an Port:", port.device)
                    self.pico = verbindung
                    return

                verbindung.close()

            except Exception as fehler:
                print("  -> Fehler:", fehler)
                if verbindung is not None and verbindung.is_open:
                    try:
                        verbindung.close()
                    except Exception:
                        pass

        raise RuntimeError("Pawlov-Leckerlispender wurde nicht gefunden.")

    # ============================================================
    # PICO AUTOMATISCH FINDEN
    # ============================================================

    


    # ============================================================
    # DIESE FUNKTION IST FÜR DIE BILDERKENNUNG WICHTIG
    # ============================================================

    def leckerli_ausgeben(self) -> bool:
            """Gibt eine Portion Leckerlis aus."""
            if self.pico is None or not self.pico.is_open:
                raise RuntimeError("Keine aktive Verbindung zum Spender vorhanden.")

            # Eventuell alte Reste im Puffer leeren
            self.pico.reset_input_buffer()
            self.pico.write(b"DISPENSE\n")
            self.pico.flush()

            antwort = self.pico.readline().decode(errors="ignore").strip()

            if antwort == "DONE":
                print("Leckerli erfolgreich ausgegeben.")
                return True
            else:
                print("WARNUNG: Keine Bestätigung vom Leckerli-Spender erhalten (Antwort:", repr(antwort), ")")
                return False



    def schliessen(self):
        """Schließt den seriellen Port sauber."""
        if self.pico and self.pico.is_open:
            self.pico.close()
            print("Verbindung zum Pawlov-Spender geschlossen.")


    # ============================================================
    # TESTPROGRAMM
    # ============================================================
    #
    # ENTER = Leckerli ausgeben
    # q + ENTER = Programm beenden
    #
    # ============================================================
