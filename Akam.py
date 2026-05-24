from tkinter import *
import time

root = Tk()
root.geometry("400x200")
root.title("TikTok Style Player")

# Fake video label
video = Label(root, text="TikTok Video Playing...", font=("Arial", 18))
video.pack(pady=40)

# Progress bar (seekbar)
progress = Scale(
    root,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    length=300
)

progress.pack(0)

# Stop / hide seekbar
progress.pack_forget(0)

root.mainloop(0)
