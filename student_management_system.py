import tkinter as tk


# ------------- COLOUR THEME -------------
BG ="#0B1120"           # Main backbround
PANEL = "#111C30"        # Frame background
BORDER = "#263750"       # Border colour
BLUE = "#2563EB"         # Primary blue
CYAN = "#22D3EE"         # Highlight colour
WHITE = "#F1F5F9"        # Main text
MUTED = "#94A3B8"        # Secondary text
INPUT_BG = "#0B1628"     # Entry background


# ------------- MAIN WINDOW  -------------
app = tk.Tk()
app.title("Student Management System")
app.geometry("1360x760")
app.configure(bg=BG)
app.resizable(False, False)

# ------------- HEADER  -------------
header = tk.Frame(app, bg=BG)
header.place(x=25, y=20, width=1310, height=75)

logo = tk.Label(
    header,
    text="S",
    font=("Segoe UI", 22, "bold"),
    bg=BLUE,
    fg=WHITE,
    width=3,
    height=1
)
logo.pack(side="left", padx=(0, 15), pady=5)

heading_area = tk.Frame(header, bg=BG)
heading_area.pack(side="left", pady=5)

heading = tk.Label(
    heading_area,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Segoe UI", 22, "bold"),
    bg=BG,
    fg=WHITE
)
heading.pack(anchor="w")

subheading = tk.Label(
    heading_area,
    text="STUDENT REGISTRATION  |  RECORDS MANAGEMENT",
    font=("Segoe UI", 10),
    bg=BG,
    fg=CYAN
)
subheading.pack(anchor="w", pady=(3, 0))

# ------------- LEFT FRAME  -------------
first_frame = tk.LabelFrame(
    app,
    text="  STUDENT DETAILS  ",
    font=("Segoe UI", 12, "bold"),
    bg=PANEL,
    fg=CYAN,
    bd=1,
    relief="solid",
    highlightbackground=BORDER,
    highlightthickness=1
)
first_frame.place(x=25, y=120, width=620, height=390)

# Left frame intoductory text
tk.Label(
    first_frame,
    text="Enter student information below",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=MUTED
).place(x=20, y=25)

# Sample layout fields - UI only
field_labels = [
    "Admission Number",
    "Student Name",
    "Gender",
    "Contact Number",
    "Class",
    "Section",
    "Disability"
]

# Labels and empty input boxes
for index, field_name in enumerate(field_labels):
    column = index % 2
    row = index // 2

    x_position = 20 + column * 295
    y_position = 70 + row * 78

    tk.Label(
        first_frame,
        text=field_name,
        font=("Segoe UI", 10, "bold"),
        bg=PANEL,
        fg=WHITE
    ).place(x=x_position, y=y_position)

    if field_name == "Gender":
        widget = tk.StringVar()

        gender_dropdown = tk.OptionMenu(
            first_frame,
            widget,
            "Male",
            "Female",
            "Other"
        )

        gender_dropdown.config(
            font=("Segoe UI", 10),
            bg=INPUT_BG,
            fg=WHITE,
            activebackground=BLUE,
            activeforeground=WHITE,
            highlightthickness=1,
        )

        gender_dropdown["menu"].config(
            bg=INPUT_BG,
            fg=WHITE
        )

        gender_dropdown.place(
            x=x_position,
            y=y_position + 25,
            width=260,
            height=32
        )

    elif field_name == "Disability":
        widget = tk.Entry(
            first_frame,
            font=("Segoe UI", 11),
            bg=INPUT_BG,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=CYAN
        )
    else:
        widget = tk.Entry(
            first_frame,
            font=("Segoe UI", 11),
            bg=INPUT_BG,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=CYAN
        )

    if field_name != "Gender":
        widget.place(
            x=x_position,
            y=y_position + 25,
            width=260,
            height=32
        )


# ------------- RIGHT FRAME  -------------
second_frame = tk.LabelFrame(
    app,
    text="  STUDENT RECORDS  ",
    font=("Segoe UI", 12, "bold"),
    bg=PANEL,
    fg=CYAN,
    bd=1,
    relief="solid",
    highlightbackground=BORDER,
    highlightthickness=1
)
second_frame.place(x=665, y=120, width=670, height=390)

tk.Label(
    second_frame,
    text="REGISTERED STUDENTS",
    font=("Segoe UI", 11, "bold"),
    bg=PANEL,
    fg=WHITE
).place(x=20, y=25)

tk.Label(
    second_frame,
    text="Student records will appear here.",
    font=("Segoe UI", 10),
    bg= PANEL,
    fg=MUTED
).place(x=20, y=65)

# place record hedings - not connected to a database
columns = [
    "Admission No.",
    "Student Name",
    "Gender",
    "Contact No.",
    "Class",
    "Section"
    ]
column_x = [10, 105, 260, 335, 440, 490, 545]
column_widths = [95, 155, 75, 105, 50, 55, 100]


for col_index, col_name in enumerate(columns):
    tk.Label(
        second_frame,
        text=col_name,
        font=("Segoe UI", 9, "bold"),
        bg="#1B2B43",
        fg=CYAN,
        anchor="w",
        padx=6,
        pady=10
    ).place(
        x=column_x[col_index],
        y=105,
        width=column_widths[col_index],
        height=38
    )

# Empty-state messaage
tk.Label(
    second_frame,
    text="No records loaded",   
    font=("Segoe UI", 11),
    bg=PANEL,
    fg=MUTED
).place(x=20, y=165)

# ------------- BOTTOM BUTTON FRAME  -------------
all_btn = tk.LabelFrame(
    app,
    text="  ACTION CENTER  ",
    font=("Segoe UI", 12, "bold"),
    bg=PANEL,
    fg=CYAN,
    bd=1,
    relief="solid",
    highlightbackground=BORDER,
    highlightthickness=1
)
all_btn.place(x=25, y=530, width=1310, height=190)

tk.Label(
    all_btn,
    text="Manage student registration and records",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=MUTED
).place(x=22, y=20)

# Button style
button_style = {
    "font": ("Segoe UI", 10, "bold"),
    "bd": 0,
    "relief": "flat",
    "cursor": "hand2",
    "width": 16,
    "height": 2
}

# UI-only buttons: commands will be connected later

# SUBMIT BUTTON
tk.Button(
    all_btn,
    text="SUBMIT",
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    activeforeground=WHITE,
    **button_style
).place(x=25, y=65)

# CLEAR BUTTON
tk.Button(
    all_btn,
    text="CLEAR",
    bg="#263750",
    fg=WHITE,
    activebackground="#334155",
    activeforeground=WHITE,
    **button_style
).place(x=235, y=65)

# UPDATE BUTTON
tk.Button(
    all_btn,
    text="UPDATE",
    bg="#0E7490",
    fg=WHITE,
    activebackground="#155E75",
    activeforeground=WHITE,
    **button_style
).place(x=445, y=65)

# DELETE BUTTON
tk.Button(
    all_btn,
    text="DELETE",
    bg="#9F1239",
    fg=WHITE,
    activebackground="#881337",
    activeforeground=WHITE,
    **button_style
).place(x=665, y=65)

# VIEW RECORDS BUTTON
tk.Button(
    all_btn,
    text="VIEW RECORDS",
    bg="#263750",
    fg=WHITE,
    activebackground="#334155",
    activeforeground=WHITE,
    **button_style
).place(x=865, y=65)

# EXIT BUTTON
tk.Button(
    all_btn,
    text="EXIT",
    bg="#263750",
    fg=WHITE,
    activebackground="#334155",
    activeforeground=WHITE,
    **button_style
).place(x=1075, y=65)

# ------------- FOOTER  -------------
footer = tk.Label(
    app,
    text="STUDENT MANAGEMENT SYSTEM  |  DESIGNED IN PYTHON TKINTER",
    font=("Segoe UI", 8),
    bg=BG,
    fg=MUTED
)
footer.place(x=25, y=730)

# ------------- RUN APPLICATION  -------------
app.mainloop()
