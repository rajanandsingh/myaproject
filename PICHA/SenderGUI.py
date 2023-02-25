#-ossso+oss+.     .:ssss:.        ./oo++++/:/      .+ssso-`   .+ssso             +s+
#/MMM:``-mMNs       dMMd         /dNy-````-oNy      -MMMo      -MMMo            /MMM+
#:MMM-   +MMM`      dMMd       `hMMs        :s      .MMMo      .MMM+           .dyMMN-
#:MMM-  `hMMh       dMMd       oMMM.         `      .MMMo``````-MMM+           y+`dMMd`
#:MMMo/ohdy/`       dMMd       dMMM`                .MMMhoooooosMMM+          /h..:NMMy
#:MMM:````          dMMd       sMMM:                .MMMo      .MMM+         .dooooyMMM+
#:MMM-              dMMd       `hMMm:       ./      .MMMo      .MMM+        `h/     sMMN:
#/MMM/              dMMd`       `+dNNh+:--/os:      -MMMs      -MMMo       `sd      `mMMm-
#-+sss+-`         .:ssss:.        `-/osss+:.        /ssso-`   ./ssso-     ./so-     -ossso:

from encode import *
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.geometry("750x400")
root.title("Personal Information as Cipher Hidden in Audio (PICHA)")
root.iconbitmap("Icon.ico")

def open_song():
    global song_path
    song_path = filedialog.askopenfilename(
        initialdir="C:/Users/Aman Pandey/OneDrive/Desktop/PICHA")
    return song_path

def open_text():
    global text_path
    text_path = filedialog.askopenfilename(
        initialdir="C:/Users/Aman Pandey/OneDrive/Desktop/PICHA")
    return text_path

def LAUNCH():
    d = part1entry.get()
    n = part2entry.get()
    encoding(d, n, song_path, text_path)  
    messagebox.showinfo("Status", "DONE\nCheck The Parent Directory")

def gen_dialog():
    public, private = gen_key(p, q)
    messagebox.showwarning(
        "THESE ARE YOUR KEYS", f"Public Key: {public} and Private Key: {private}\nKEEP THEM SAFE")


heading = Label(text="Steganographic Encoding", font="algerian 16 ")
heading.grid(row=0, column=3)


button_img = PhotoImage(file='button.png')
generate_btn = Button(root, image=button_img,
                      command=gen_dialog, borderwidth=0)
generate_btn.grid(row=1, column=3)

search_song = Label(root, text="UPLOAD THE SONG: -",
                    font="comicsansms 12 ", padx=5, pady=20)
search_song.grid(row=1, column=0)

search_text = Label(root, text="UPLOAD THE TEXT: -",
                    font="comicsansms 12 ", padx=5, pady=20)
search_text.grid(row=2, column=0)

public = Label(root, text="Enter The Public Key: -",
               font="comicsansms 12 ", padx=5, pady=20)
public.grid(row=3, column=0)


part1entry = IntVar()
part1 = Entry(root, width=10, relief=SUNKEN,
              borderwidth=3, textvariable=part1entry)
part1.grid(row=3, column=1)


part2entry = IntVar()
part2 = Entry(root, width=10, relief=SUNKEN,
              borderwidth=3, textvariable=part2entry)
part2.grid(row=3, column=2)


upload_btn = PhotoImage(file="upload.png")

song_btn = Button(root, image=upload_btn, command=open_song, borderwidth=0)
song_btn.grid(row=1, column=2)

text_btn = Button(root, image=upload_btn, command=open_text, borderwidth=0)
text_btn.grid(row=2, column=2)

launch_img = PhotoImage(file="Launch.png")
launch = Button(root, image=launch_img, command=LAUNCH, borderwidth=0)
launch.grid(row=4, column=3)

root.mainloop()
