import customtkinter as ctk

# --------------------------------------------------
# GRUNDEINSTELLUNGEN
# --------------------------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Farben

BACKGROUND_COLOR = "#B9CFBA"
MENU_COLOR = "#546B53"
BUTTON_COLOR = "#546B53"
BUTTON_HOVER_COLOR = "#37513F"
BUTTON_ACTIVE_COLOR = "#37513F"
TEXT_COLOR = "#27201C"


# --------------------------------------------------
# HAUPTFENSTER
# --------------------------------------------------

app = ctk.CTk()

app.title("PAWLOV: Tierisch gut trainieren")
app.geometry("900x600")
app.minsize(700, 500)

app.configure(fg_color=BACKGROUND_COLOR)

#---------------Menü Code ----------------------#
MENU_WIDTH = 250
menu_open = False


menu_frame = ctk.CTkFrame(
    app,
    width=MENU_WIDTH,

    fg_color=MENU_COLOR,
    corner_radius=0
)

# Menü zunächst außerhalb des Fensters
menu_frame.place(x=-MENU_WIDTH, y=0, relheight=1)


def toggle_menu():
    global menu_open

    if menu_open:
        slide_menu_out()
    else:
        slide_menu_in()


def slide_menu_in():
    global menu_open
    menu_open = True
    menu_button.configure(bg_color=MENU_COLOR)
    animate_menu(-MENU_WIDTH, 0)


def slide_menu_out():
    global menu_open
    menu_open = False
    menu_button.configure(bg_color=BACKGROUND_COLOR)
    animate_menu(0, -MENU_WIDTH)


def animate_menu(start, target):

    step = 20

    if start < target:
        new_x = min(start + step, target)
    else:
        new_x = max(start - step, target)

    menu_frame.place(x=new_x, y=0)

    if new_x != target:
        app.after(
            10,
            lambda: animate_menu(new_x, target)
        )

#---------------------Menü Button --------------------#
menu_button = ctk.CTkButton(
    app,
    text="☰",
    width=50,
    height=50,
    corner_radius=10,

    fg_color=BACKGROUND_COLOR,
    hover_color="#DDDDDD",
    text_color=TEXT_COLOR,

    font=ctk.CTkFont(size=28),

    command=toggle_menu
)

menu_button.place(x=20, y=20)

#---------------------Menü Inhalt --------------------#
#Menü buttons: Tricks, Training, Statistik, Einstellungen:
Tricks_button = ctk.CTkButton(
    menu_frame,
    text="Tricks",
    width=200,
    height=50,
    corner_radius=10,

    fg_color=MENU_COLOR,
    hover_color="#37513F",
    text_color=TEXT_COLOR,

    font=ctk.CTkFont(size=20),

)
Training_button = ctk.CTkButton(
    menu_frame,
    text="Training",
    width=200,
    height=50,
    corner_radius=10,

    fg_color=MENU_COLOR,
    hover_color="#37513F",
    text_color=TEXT_COLOR,

    font=ctk.CTkFont(size=20),

)
Statistik_button = ctk.CTkButton(
    menu_frame,
    text="Statistik",
    width=200,
    height=50,
    corner_radius=10,

    fg_color=MENU_COLOR,
    hover_color="#37513F",
    text_color=TEXT_COLOR,

    font=ctk.CTkFont(size=20),

)
Einstellungen_button = ctk.CTkButton(
    menu_frame,
    text="Einstellungen",
    width=200,
    height=50,
    corner_radius=10,

    fg_color=MENU_COLOR,
    hover_color="#37513F",
    text_color=TEXT_COLOR,

    font=ctk.CTkFont(size=20),

)
#Buttons anzeigen:
Tricks_button.pack(pady=(100, 10))  
Training_button.pack(pady=10)
Statistik_button.pack(pady=10)
Einstellungen_button.pack(pady=10)

# --------------------------------------------------
# BUTTON FUNKTION
# --------------------------------------------------

active_button = None


def select_button(button):
    global active_button

    # Alten Button zurücksetzen
    if active_button is not None:
        active_button.configure(fg_color=BUTTON_COLOR)

    # Neuen Button markieren
    button.configure(fg_color=BUTTON_ACTIVE_COLOR)

    active_button = button


# --------------------------------------------------
# ÜBERSCHRIFT
# --------------------------------------------------

title = ctk.CTkLabel(
    app,
    text="PAWLOV",
    font=ctk.CTkFont(
        family="Arial",
        size=48,
        weight="bold"
    ),
    text_color=TEXT_COLOR
)

title.pack(pady=(60, 50))


# --------------------------------------------------
# BUTTON-BEREICH
# --------------------------------------------------

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

button_frame.pack(expand=True)


# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

buttons = []

for i in range(1, 5):

    button = ctk.CTkButton(
        button_frame,
        text=str(i),

        width=180,
        height=130,

        corner_radius=25,

        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,

        text_color=TEXT_COLOR,

        font=ctk.CTkFont(
            size=36,
            weight="bold"
        )
    )

    # Button-Funktion erst nach Erstellung setzen
    button.configure(
        command=lambda b=button: select_button(b)
    )

    buttons.append(button)


# --------------------------------------------------
# 2 x 2 ANORDNUNG
# --------------------------------------------------

buttons[0].grid(row=0, column=0, padx=20, pady=20)
buttons[1].grid(row=0, column=1, padx=20, pady=20)

buttons[2].grid(row=1, column=0, padx=20, pady=20)
buttons[3].grid(row=1, column=1, padx=20, pady=20)


# --------------------------------------------------
# PROGRAMM STARTEN
# --------------------------------------------------

app.mainloop()