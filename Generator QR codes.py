import qrcode
import tkinter as tk
from PIL import ImageTk, Image

def generate_qr_code():
    text = entry.get()  
    qr = qrcode.QRCode(version=1, box_size=10, border=4)  
    qr.add_data(text)  
    qr.make(fit=True)
    
    
    img = qr.make_image(fill_color="black", back_color="white") 
    window = tk.Toplevel()
    window.title("QR Code")
    window.configure(bg='white')
    window.geometry("400x400")

  
    qr_frame = tk.Frame(window, bg='white')
    qr_frame.pack(pady=10)
    img_tk = ImageTk.PhotoImage(img.resize((380, 380)))
    label = tk.Label(qr_frame, image=img_tk, bg='white')
    label.image = img_tk
    label.pack()

root = tk.Tk()
root.title("Generate QR Code")
root.configure(bg='#212121')
root.geometry("400x200")

input_frame = tk.Frame(root, bg='#212121')
input_frame.pack(expand=True)

entry = tk.Entry(input_frame, font=('Helvetica', 14), bg='white', fg='#212121', borderwidth=0, width=20, justify='center')
entry.pack(pady=10, ipady=5)

button = tk.Button(input_frame, text="Generate", font=('Helvetica', 12), command=generate_qr_code, bg='#FFD700', fg='#212121', activebackground='#FFD700', activeforeground='#212121', padx=20, pady=5, relief='flat')
button.pack()

root.mainloop()
