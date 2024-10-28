import openai
import tkinter as tk
from tkinter import scrolledtext, font
from PIL import Image, ImageTk

openai.api_key = "Put your API key here: "

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def send_message():
    user_input = entry.get()
    if user_input.lower() in ["quit", "exit", "bye", "leave", "goodbye"]:
        root.quit()
    else:
        add_message(user_input, "user")
        response = chat_with_gpt(user_input)
        add_message(response, "AbhiBot")
        entry.delete(0, tk.END)
        chat_area.yview(tk.END)

def add_message(message, sender):
    avatar = user_avatar if sender == "user" else bot_avatar
    chat_area.image_create(tk.END, image=avatar)
    chat_area.insert(tk.END, f"{sender.capitalize()}: {message}\n", sender)
    chat_area.insert(tk.END, "-------------------------------------------------------------------------------------------------------------------\n", "info")

root = tk.Tk()
root.title("AbhiBot")
root.geometry("600x500")
root.configure(bg="#D1E7DD")

user_avatar = ImageTk.PhotoImage(Image.open("C:\\Users\\abhit\\Chatbot Test\\user.png").resize((30, 30)))
bot_avatar = ImageTk.PhotoImage(Image.open("C:\\Users\\abhit\\Chatbot Test\\bot.png").resize((30, 30)))

chat_font = font.Font(family="Comic Sans MS", size=12)
entry_font = font.Font(family="Comic Sans MS", size=12)

frame = tk.Frame(root, bg="#D1E7DD")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=chat_font, bg="#F0F8FF", fg="black", bd=0)
chat_area.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="red", background="turquoise")
chat_area.tag_config("AbhiBot", foreground="navy", background="gold")
chat_area.tag_config("info", foreground="black", background="lavender")
chat_area.tag_config("info1", foreground="navy", background="lavender")

chat_area.insert(tk.END, "                                                                                       \-------------------------------------------------/ \n", "info1")
chat_area.insert(tk.END, "                                                                                       |Enter a prompt to begin chatting with AbhiBot| \n", "info")
chat_area.insert(tk.END, "                                                                                       /-------------------------------------------------\ \n", "info1")

entry_frame = tk.Frame(root, bg="#D1E7DD")
entry_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

entry = tk.Entry(entry_frame, font=entry_font, bg="#F0F8FF")
entry.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Comic Sans MS", 10), bg="#5BC0DE", fg="white", activebackground="#31B0D5")
send_button.pack(side=tk.LEFT)

clear_button = tk.Button(entry_frame, text="Clear", command=lambda: chat_area.delete(1.0, tk.END), font=("Comic Sans MS", 10), bg="#D9534F", fg="white", activebackground="#C9302C")
clear_button.pack(side=tk.LEFT, padx=(5, 0))

exit_button = tk.Button(entry_frame, text="Exit", command=root.quit, font=("Comic Sans MS", 10), bg="#D9534F", fg="white", activebackground="#C9302C")
exit_button.pack(side=tk.LEFT, padx=(5, 0))

root.mainloop()