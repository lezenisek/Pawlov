import customtkinter as ctk
from colors import *

# --------------------------------------------------
# FARBEN
# --------------------------------------------------



# --------------------------------------------------
# SEITE "MEINE TIERE"
# --------------------------------------------------

class MeineTierePage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=BACKGROUND_COLOR,
            corner_radius=0
        )

        # Überschrift
        title = ctk.CTkLabel(
            self,
            text="PAWLOV",
            font=ctk.CTkFont(
                size=42,
                weight="bold"
            ),
            text_color=TEXT_COLOR
        )

        title.pack(pady=(40, 10))


        # Seitenüberschrift
        page_title = ctk.CTkLabel(
            self,
            text="Meine Tiere",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            ),
            text_color=TEXT_COLOR
        )

        page_title.pack(pady=(10, 30))


        # --------------------------------------------------
        # BEREICH FÜR GESPEICHERTE TIERE
        # --------------------------------------------------

        self.tiere_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.tiere_frame.pack(
            pady=10
        )


        # --------------------------------------------------
        # NEUES TIER BUTTON
        # --------------------------------------------------

        self.neues_tier_button = ctk.CTkButton(
            self,
            text="+ Neues Tier anlegen",

            width=250,
            height=60,

            corner_radius=12,

            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,

            text_color=TEXT_COLOR,

            font=ctk.CTkFont(
                size=18,
                weight="bold"
            ),

            command=self.formular_anzeigen
        )

        self.neues_tier_button.pack(
            pady=30
        )


        # --------------------------------------------------
        # FORMULAR
        # --------------------------------------------------

        self.formular_frame = ctk.CTkFrame(
            self,
            fg_color=CARD_COLOR,
            corner_radius=15
        )

        # Noch NICHT packen!
        # Das Formular soll erst nach Klick erscheinen.


        # NAME

        name_label = ctk.CTkLabel(
            self.formular_frame,
            text="Name",
            text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=16)
        )

        name_label.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        self.name_entry = ctk.CTkEntry(
            self.formular_frame,
            width=300,
            height=40,
            placeholder_text="Name des Tieres"
        )

        self.name_entry.pack(
            padx=30
        )


        # GEBURTSTAG

        geburtstag_label = ctk.CTkLabel(
            self.formular_frame,
            text="Geburtstag",
            text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=16)
        )

        geburtstag_label.pack(
            anchor="w",
            padx=30,
            pady=(15, 5)
        )

        self.geburtstag_entry = ctk.CTkEntry(
            self.formular_frame,
            width=300,
            height=40,
            placeholder_text="TT.MM.JJJJ"
        )

        self.geburtstag_entry.pack(
            padx=30
        )


        # GESCHLECHT

        geschlecht_label = ctk.CTkLabel(
            self.formular_frame,
            text="Geschlecht",
            text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=16)
        )

        geschlecht_label.pack(
            anchor="w",
            padx=30,
            pady=(15, 5)
        )

        self.geschlecht_menu = ctk.CTkOptionMenu(
            self.formular_frame,

            values=[
                "weiblich",
                "männlich"
            ],

            width=300,
            height=40,
            
            fg_color="#343638",
            button_color="#343638",
            button_hover_color="#444648",

            text_color="white",

            dropdown_fg_color="#343638",
            dropdown_hover_color="#444648",
            dropdown_text_color="white"
        )

        self.geschlecht_menu.pack(
            padx=30
        )


        # TIERART

        tierart_label = ctk.CTkLabel(
            self.formular_frame,
            text="Tierart",
            text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=16)
        )

        tierart_label.pack(
            anchor="w",
            padx=30,
            pady=(15, 5)
        )

        self.tierart_menu = ctk.CTkOptionMenu(
            self.formular_frame,

            values=[
                "Katze",
                "Kaninchen"
            ],

            width=300,
            height=40,
            
            fg_color="#343638",
            button_color="#343638",
            button_hover_color="#444648",

            text_color="white",

            dropdown_fg_color="#343638",
            dropdown_hover_color="#444648",
            dropdown_text_color="white"
        )

        self.tierart_menu.pack(
            padx=30
        )


        # SPEICHERN

        speichern_button = ctk.CTkButton(
            self.formular_frame,

            text="Tier speichern",

            width=300,
            height=45,

            corner_radius=10,

            fg_color=BACKGROUND_COLOR,
            hover_color="#3E5845",

            text_color=TEXT_COLOR,

            font=ctk.CTkFont(
                size=16,
                weight="bold"
            ),

            command=self.tier_speichern
        )

        speichern_button.pack(
            padx=30,
            pady=30
        )


    # --------------------------------------------------
    # FORMULAR ANZEIGEN
    # --------------------------------------------------

    def formular_anzeigen(self):

        self.neues_tier_button.pack_forget()

        self.formular_frame.pack(
            pady=20
        )


    # --------------------------------------------------
    # TIER SPEICHERN
    # --------------------------------------------------

    def tier_speichern(self):

        name = self.name_entry.get()
        geburtstag = self.geburtstag_entry.get()
        geschlecht = self.geschlecht_menu.get()
        tierart = self.tierart_menu.get()

        print("Tier gespeichert:")
        print("Name:", name)
        print("Geburtstag:", geburtstag)
        print("Geschlecht:", geschlecht)
        print("Tierart:", tierart)

        # Tier als Button anzeigen
        tier_button = ctk.CTkButton(
            self.tiere_frame,

            text=f"{tierart}\n{name}",

            width=180,
            height=100,

            corner_radius=15,

            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,

            text_color=TEXT_COLOR,

            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        tier_button.pack(
            side="left",
            padx=10,
            pady=10
        )


        # Formular wieder verstecken
        self.formular_frame.pack_forget()

        # Button wieder anzeigen
        self.neues_tier_button.pack(
            pady=30
        )


        # Eingabefelder leeren
        self.name_entry.delete(0, "end")
        self.geburtstag_entry.delete(0, "end")