import tkinter as tk

def km_to_mile():
    km = float(entry.get())
    miles = km * 0.621371
    result_label.config(text=f"{km} km is {miles:.2f} miles")

def mile_to_km():
    mile = float(entry.get())
    km = mile / 0.621371
    result_label.config(text=f"{mile} miles is {km:.2f} km")

root = tk.Tk()
root.title("Distance Converter")

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

km_to_mile_button = tk.Button(root, text="Km to Mile", command=km_to_mile)
km_to_mile_button.pack(padx=10, pady=5)

mile_to_km_button = tk.Button(root, text="Mile to Km", command=mile_to_km)
mile_to_km_button.pack(padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=10)

root.mainloop()
