# GUI Libary
import customtkinter
import tkinter
import script
import pyaudio

p = pyaudio.PyAudio()
default_device =  p.get_default_input_device_info()


# THEME APPARENCE
customtkinter.set_appearance_mode("default")
customtkinter.set_default_color_theme("blue")


# ROOT & WINDOW INFO
van1 = customtkinter.CTk()
van1.resizable(False, False)
van1.title("Default Microphone Detector")
van1.geometry('300x100')
van1.overrideredirect(False)


# PRINT INSIDE THE GUI
INPUT1 = customtkinter.CTkLabel(master=van1, text=default_device['name'], font=('Roboto', 15, 'bold'))
INPUT1.pack
INPUT1.place(x=60, y=30)



# MAIN LOOP
van1.mainloop()
