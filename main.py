import customtkinter as c

FONT_NAME = "Courier"

root = c.CTk()
c.set_appearance_mode("Dark")
c.set_default_color_theme("dark-blue")
root.title("Type racer")
root.config(padx=100, pady=50)

time_label = c.CTkLabel(master=root,text=40, font=(FONT_NAME,50))
time_label.pack()

text_frame = c.CTkFrame(master=root)
text_frame.pack(fill="both", expand=True)

text_label = c.CTkLabel(master=text_frame, text="TEST TEST TEST TEST", font=(FONT_NAME, 30))
text_label.pack(pady=25)

text_entry = c.CTkEntry(master=root)
text_entry.pack(pady=50, fill="x")

button_frame = c.CTkFrame(master=root)
button_frame.pack(fill="both")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.rowconfigure(0,weight=0)
start_button = c.CTkButton(master=button_frame, text="Start")
start_button.grid(row=0, column=0,sticky="w")

reset_button = c.CTkButton(master=button_frame, text="Reset")
reset_button.grid(row=0, column=1, sticky="e")

root.mainloop()
