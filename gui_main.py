import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def authenticate(username, password):
    # Add your authentication logic here
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def on_login_click():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Incomplete Information", "Please enter both username and password.")
    else:
        authenticate(username, password)

# Create main window
root = tk.Tk()
root.title("Parking System Admin Login")

# Create a white canvas for the entire window
canvas = tk.Canvas(root, bg="white", width=800, height=400)
canvas.pack(expand="true", fill="both")

# Resize and load background image
original_image = Image.open("background_image.png")
resized_image = original_image.resize((398, 332))
background_photo = ImageTk.PhotoImage(resized_image)

# Display background image on the canvas
canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Create login frame on the right side
login_frame = ttk.Frame(root, padding="20", style="TFrame")  # Added a ttk style to frame
login_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=1)

# Create and place widgets on the login frame
admin_title_label = ttk.Label(login_frame, text="Admin Login", font=("Helvetica", 20, "bold"), style="TLabel")  # Added a ttk style to label
admin_title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

username_label = ttk.Label(login_frame, text="Username:", font=("Helvetica", 14), style="TLabel")  # Added a ttk style to label
username_label.grid(row=1, column=0, sticky="w", pady=(0, 5))

username_entry = ttk.Entry(login_frame, font=("Helvetica", 14))  # Increased font size
username_entry.grid(row=1, column=1, sticky="ew", pady=(0, 5))

password_label = ttk.Label(login_frame, text="Password:", font=("Helvetica", 14), style="TLabel")  # Added a ttk style to label
password_label.grid(row=2, column=0, sticky="w", pady=(0, 10))

password_entry = ttk.Entry(login_frame, show="*", font=("Helvetica", 14))  # Increased font size
password_entry.grid(row=2, column=1, sticky="ew", pady=(0, 10))

login_button = ttk.Button(login_frame, text="Login", command=on_login_click, style="TButton")  # Added a ttk style to button
login_button.grid(row=3, column=1, sticky="ew", pady=(10, 0))

# Adjust column weights to make the login frame expandable
login_frame.columnconfigure(1, weight=1)

# Set the main window size based on the image and frame size
root.geometry("{}x{}+{}+{}".format(800, 400, int((root.winfo_screenwidth() - 800) / 2), int((root.winfo_screenheight() - 400) / 2)))

# Run the Tkinter event loop
root.mainloop()