from Tkinter import *
import datetime

toggle = True
active_class = ''

def blink():
    global toggle
    global active_class
    if toggle:
        w.configure(text='')
    else:
        w.configure(text=active_class)
    toggle = not toggle
    root.after(480, blink)



def task():
    global active_class
    now = datetime.datetime.now()
    now = datetime.time(hour=now.hour, minute=now.minute, second=0)

    paud_start = datetime.time(8, 0, 0)
    paud_end = datetime.time(8, 30, 0)

    sd1_3_start = datetime.time(8, 30, 0)
    sd1_3_end = datetime.time(9, 0, 0)

    sd4_6_start = datetime.time(9, 0, 0)
    sd4_6_end = datetime.time(9, 30, 0)

    smp_start = datetime.time(9, 30, 0)
    smp_end = datetime.time(10, 0, 0)

    sma_start = datetime.time(10, 0, 0)
    sma_end = datetime.time(10, 30, 0)

    active_class = jenjang[0]
    if time_in_range(paud_start, paud_end, now):
        active_class = jenjang[0]
    if time_in_range(sd1_3_start, sd1_3_end, now):
        active_class = jenjang[1]
    if time_in_range(sd4_6_start, sd4_6_end, now):
        active_class = jenjang[2]
    if time_in_range(smp_start, smp_end, now):
        active_class = jenjang[3]
    if time_in_range(sma_start, sma_end, now):
        active_class = jenjang[4]

    w.configure(text=active_class)
    root.after(60000, task)






def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

root = Tk()
jenjang = ['PAUD', 'SD KELAS 1-3', 'SD KELAS 4-6', 'SMP KELAS 7-9', 'SMA KELAS 10-12']


end = datetime.time(1, 0, 0)
w = Label(root, text="PAUD", fg="red", bg='black')
w.config(font='Helvetica 50 bold')
task()
blink()

w.pack()
root.configure(background='black')
root.mainloop()