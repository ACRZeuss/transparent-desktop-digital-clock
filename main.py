# Kütüphanelerim import edilmesi
import string
from tkinter import Label, mainloop, Tk
from datetime import datetime

# Ana pencere oluşturma
root = Tk()
root.title("Digital Clock")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()


# Saatin anlık olarak değişip içeriğinin düzenlenmesini ve Labela entegre olmasını sağlama
def time():
    now = datetime.now()
    dots = [":", " "]
    seconds = datetime.strftime(now, "%S")
    if (int(seconds) % 2) == 0:
        dt_1 = str(dots[1])
        dot = (dt_1)
    else:
        dt_2 = str(dots[1])
        dot = (dt_2)
    string = datetime.strftime(now, "%A, %b %d\n%I{0}%M{1}%S %p".format(dot, dot))
    label_time.config(text=string, justify="center")
    label_time.after(1000, time)

# Label widgetını düzenliyoruz
label_time = Label(
    root,
    font=("digital numbers", 65),
    background="#000000",
    foreground="#ffffff",
    width=width,
    height=height
)
label_time.pack(anchor="center")
label_time.master.overrideredirect(True)
label_time.master.wm_attributes("-transparentcolor", "#000000")
label_time.master.lift()


# time fonksiyonunu burada başlatıyoruz.
time()

# Ana pencere özellikleri hakkında düzenleme
root.eval('tk::PlaceWindow . center')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes("-fullscreen", True)

# Ana pencere dongüsünü başlatma
mainloop()