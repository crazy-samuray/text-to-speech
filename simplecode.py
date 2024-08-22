import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        lang = 'tr'
        speech = gTTS(text=text, lang=lang, slow=False)
        speech.save("output.mp3")
        os.system("start output.mp3")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir metin giriniz!")


window = tk.Tk()
window.title("Text to Speech")

text_entry = tk.Text(window, height=10, width=50)
text_entry.pack(pady=10)

speak_button = tk.Button(window, text="Sesi Çal", command=text_to_speech)
speak_button.pack(pady=10)

window.mainloop()