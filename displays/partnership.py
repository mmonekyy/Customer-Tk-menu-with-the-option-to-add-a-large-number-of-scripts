import customtkinter
import subprocess

def main(frame_right):
    venv_python = '.venv\Scripts\python.exe'
    for widget in frame_right.winfo_children():
        widget.destroy()

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
        if process is None or process.poll() is not None: 
            process = subprocess.Popen([venv_python, "partnerships/print.py"])  

    def stop():
        global process
        if process is not None:
            process.terminate()

    buttons = customtkinter.CTkFrame(frame_right)
    buttons.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    text = customtkinter.CTkFrame(frame_right)
    text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    button1 = customtkinter.CTkButton(buttons, text="Start", command=start)
    button2 = customtkinter.CTkButton(buttons, text="Stop", command=stop)

    check_box = customtkinter.CTkCheckBox(buttons, text="Servers rn1",)
    check_box1 = customtkinter.CTkCheckBox(buttons, text="Servers rn2",)
    check_box2 = customtkinter.CTkCheckBox(buttons, text="Servers rn3",)
    check_box3 = customtkinter.CTkCheckBox(buttons, text="Servers rn4",)

    label = customtkinter.CTkLabel(buttons, text="Status: Not Running",)
    label1 = customtkinter.CTkLabel(buttons, text="Status: Not Running",)
    label2 = customtkinter.CTkLabel(buttons, text="Status: Not Running",)
    label3 = customtkinter.CTkLabel(buttons, text="Status: Not Running",)

    textbox = customtkinter.CTkTextbox(master=text)

    button1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
    button2.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    check_box.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    check_box1.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    check_box2.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    check_box3.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    label1.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    label2.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    label3.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    textbox.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    frame_right.grid_rowconfigure(0, weight=1)
    frame_right.grid_rowconfigure(1, weight=3)
    frame_right.grid_columnconfigure(0, weight=1)

    buttons.grid_rowconfigure(0, weight=1)
    buttons.grid_columnconfigure(0, weight=1)
    buttons.grid_columnconfigure(1, weight=1)

    buttons.grid_columnconfigure(0, weight=1, minsize=100)  
    buttons.grid_columnconfigure(1, weight=1, minsize=100)  

    text.grid_rowconfigure(0, weight=1)
    text.grid_columnconfigure(0, weight=1)
