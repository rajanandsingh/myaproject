
#-ossso+oss+.     .:ssss:.        ./oo++++/:/      .+ssso-`   .+ssso             +s+
#/MMM:``-mMNs       dMMd         /dNy-````-oNy      -MMMo      -MMMo            /MMM+
#:MMM-   +MMM`      dMMd       `hMMs        :s      .MMMo      .MMM+           .dyMMN-
#:MMM-  `hMMh       dMMd       oMMM.         `      .MMMo``````-MMM+           y+`dMMd`
#:MMMo/ohdy/`       dMMd       dMMM`                .MMMhoooooosMMM+          /h..:NMMy
#:MMM:````          dMMd       sMMM:                .MMMo      .MMM+         .dooooyMMM+
#:MMM-              dMMd       `hMMm:       ./      .MMMo      .MMM+        `h/     sMMN:
#/MMM/              dMMd`       `+dNNh+:--/os:      -MMMs      -MMMo       `sd      `mMMm-
#-+sss+-`         .:ssss:.        `-/osss+:.        /ssso-`   ./ssso-     ./so-     -ossso:


from extract import *
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.geometry("750x350")
root.title("Personal Information as Cipher Hidden in Audio (PICHA)")
root.iconbitmap("Icon.ico")


def LAUNCH():
    d = part1entry.get()
    n = part2entry.get()
    extraction(d, n)
    messagebox.showinfo("Status", "DONE\nCheck The Parent Directory")


def open_song():
    global song_path
    song_path = filedialog.askopenfilename(
        initialdir="C:/Users/Aman Pandey/OneDrive/Desktop/PICHA")
    return song_path


heading = Label(text="Steganographic Extraction", font="algerian 16 ")
heading.grid(row=0, column=3)

song_text = Label(root, text="UPLOAD THE SONG: -",
                  font="comicsansms 12", padx=5, pady=20)
song_text.grid(row=1, column=0)

Private = Label(root, text="Enter The Private Key: -",
               font="comicsansms 12 ", padx=5, pady=20)
Private.grid(row=2, column=0)

part1entry = IntVar()
part1 = Entry(root, width=10, relief=SUNKEN,
              borderwidth=3, textvariable=part1entry)
part1.grid(row=2, column=1)

part2entry = IntVar()
part2 = Entry(root, width=10, relief=SUNKEN,
              borderwidth=3, textvariable=part2entry)
part2.grid(row=2, column=2)

upload_btn = PhotoImage(file="upload.png")
song_btn = Button(root, image=upload_btn, command=open_song, borderwidth=0)
song_btn.grid(row=1, column=2)

launch_img = PhotoImage(file="Launch.png")
launch = Button(root, image=launch_img, command=LAUNCH, borderwidth=0)
launch.grid(row=4, column=3)
root.mainloop()
