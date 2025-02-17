import customtkinter
import subprocess

def main(frame_right):
    venv_python = '.venv\Scripts\python.exe'
    # Clear previous widgets
    for widget in frame_right.winfo_children():
        widget.destroy()

    # Set the frame size and prevent resizing of widgets within it
    frame_right.grid_propagate(False)
    frame_right.configure(width=510, height=400)

    global process
    process = None

    def start():
        print("checkbox toggled, current value:", check_box.get())
        print("checkbox toggled, current value:", check_box1.get())
        print("checkbox toggled, current value:", check_box2.get())
        print("checkbox toggled, current value:", check_box3.get())
        with open("partnerships/servers","w") as f:
            f.write(f"{check_box.get()}{check_box1.get()}{check_box2.get()}{check_box3.get()}")
        print("-" * 100)
        global process
        if process is None or process.poll() is not None:  # Run only if process is not running
            process = subprocess.Popen([venv_python, "partnerships/print.py"])  # Run the second script

    def stop():
        global process
        if process is not None:
            process.terminate()

    # Create a frame for buttons and status labels
    buttons = customtkinter.CTkFrame(frame_right)
    buttons.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Create a frame for the text area (output textbox)
    text = customtkinter.CTkFrame(frame_right)
    text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Create buttons with equal width
    button1 = customtkinter.CTkButton(buttons, text="Start", command=start)
    button2 = customtkinter.CTkButton(buttons, text="Stop", command=stop)

    # Create checkboxes for servers
    check_box = customtkinter.CTkCheckBox(buttons, text="Servers rn1",)
    check_box1 = customtkinter.CTkCheckBox(buttons, text="Servers rn2",)
    check_box2 = customtkinter.CTkCheckBox(buttons, text="Servers rn3",)
    check_box3 = customtkinter.CTkCheckBox(buttons, text="Servers rn4",)

    # Create labels for server status
    label = customtkinter.CTkLabel(buttons, text="Status: Not Running",)
    label1 = customtkinter.CTkLabel(buttons, text="Status: Not Running",)
    label2 = customtkinter.CTkLabel(buttons, text="Status: Not Running",)
    label3 = customtkinter.CTkLabel(buttons, text="Status: Not Running",)

    # Create a textbox for output
    textbox = customtkinter.CTkTextbox(master=text)

    # Grid configuration for buttons
    button1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
    button2.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Grid configuration for checkboxes
    check_box.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    check_box1.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    check_box2.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    check_box3.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    # Grid configuration for labels
    label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    label1.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    label2.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    label3.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    # Grid configuration for textbox
    textbox.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Adjust grid column/row weights to allow resizing
    frame_right.grid_rowconfigure(0, weight=1)
    frame_right.grid_rowconfigure(1, weight=3)
    frame_right.grid_columnconfigure(0, weight=1)

    # Make buttons and checkboxes scale properly
    buttons.grid_rowconfigure(0, weight=1)
    buttons.grid_columnconfigure(0, weight=1)
    buttons.grid_columnconfigure(1, weight=1)

    # Ensure equal width for the buttons
    buttons.grid_columnconfigure(0, weight=1, minsize=100)  # Ensure equal width for button1
    buttons.grid_columnconfigure(1, weight=1, minsize=100)  # Ensure equal width for button2

    text.grid_rowconfigure(0, weight=1)
    text.grid_columnconfigure(0, weight=1)
