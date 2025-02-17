import customtkinter
import os
import importlib.util

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.title('Menu')
app.geometry("800x450")
app.maxsize(800, 450)
app.minsize(800, 450)

frame_left = customtkinter.CTkFrame(app, width=240, height=450)
frame_left.grid(row=0, column=0, padx=(0, 15), sticky="nsew")

scrollable_frame = customtkinter.CTkScrollableFrame(frame_left, width=240, height=440)
scrollable_frame.grid(row=0, column=0, sticky="nsew")

scrollable_frame.grid_rowconfigure(0, weight=1)
scrollable_frame.grid_columnconfigure(0, weight=1)

# Prawa ramka
frame_right = customtkinter.CTkFrame(app, width=500, height=400)
frame_right.grid(row=0, column=1, pady=10, sticky="nsew")

def load_modules(folder):
    modules = {}
    for filename in os.listdir(folder):
        if filename.endswith(".py"):  
            module_name = filename[:-3] 
            module_path = os.path.join(folder, filename)
            try:
                # Ładowanie modułu
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "main"): 
                    modules[module_name] = module.main
            except Exception as e:
                print(f"Nie udało się załadować modułu {module_name}: {e}")
    return modules

modules = load_modules("displays")

def cwelnia(value):
    print(f"Kliknięto przycisk z wartością: {value}")
    if value in modules:
        modules[value](frame_right)  

for i, module_name in enumerate(modules.keys()):
    button = customtkinter.CTkButton(
        scrollable_frame,
        text=f"{module_name}",
        command=lambda value=module_name: cwelnia(value)  
    )
    button.grid(row=i, column=0, padx=5, pady=5, sticky="nsew")

app.mainloop()
