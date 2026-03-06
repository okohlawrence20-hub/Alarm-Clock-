import customtkinter as ctk

import time

import winsound

clock = ctk.CTk()

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

clock.title("Clock")

clock.geometry("400x400")

clock_label = ctk.CTkLabel(clock,text = "Alarm Clock", font=("Arial", 30,), text_color = "#09189E")
clock_label.pack(pady=8, padx= 10)

alarm_triggered = False
def ock():
    global alarm_triggered

    h = time.strftime("%H:%M")
    s = time.strftime("%S")
    a = time.strftime("%A")
    p = time.strftime("%p")
    z = time.strftime("%Z")
    clock_label.configure(text = f"{h}:{s} {p}")

    day.configure(text=f"{a} : {z}")

    alarm = str(clock_entry.get())
    if alarm == h and not alarm_triggered:
            f = 4000
            d = 2000
            winsound.Beep (f, d)

    
    clock_label.after(1000, ock)

def stop_alarm():
         global alarm_triggered

         alarm_triggered =  True
     
clock_label = ctk.CTkLabel(clock, text="", font=("Arial", 30), fg_color="#121F7D", height= 100, width=100, corner_radius=50)
clock_label.pack(pady=10, padx=20)

day = ctk.CTkLabel (clock, text="", font=("Arial", 20, "bold"), text_color= "#121F7D")
day.pack(pady=5)

alarm_label = ctk.CTkLabel (clock, text="Enter Your Alarm", font=("Arial", 17), text_color= "#121F7D")
alarm_label.pack(pady=3)

def alarm():
    alarm = str(clock_entry.get())
    alarm_label2.configure(text=f"You Alarm will ring at: {alarm} ")

clock_entry = ctk.CTkEntry(clock, corner_radius = 40, placeholder_text="eg 11:30")
clock_entry.pack(pady=4)

alarm_frame = ctk.CTkFrame(clock)
alarm_frame.pack(pady=5)

clock_button = ctk.CTkButton(alarm_frame, text="Start", fg_color="#121F7D", command = alarm, width=60,height=60, corner_radius=30)
clock_button.grid(row=0, column=0, padx=5)

stop_button = ctk.CTkButton(alarm_frame, text="Stop", fg_color="#121F7D", command = stop_alarm, width=60,height=60, corner_radius=30)
stop_button.grid(row=0, column=1, padx=5)

alarm_label2 = ctk.CTkLabel (clock, text="", font=("Arial", 17), text_color= "#FFFFFF", fg_color="#121F7D")
alarm_label2.pack(pady=3, padx =10)


ock()
clock.mainloop()
