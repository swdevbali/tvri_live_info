from Tkinter import *
import datetime


def task():
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

    if time_in_range(paud_start, paud_end, now):
        w.configure(text=jenjang[0])
    if time_in_range(sd1_3_start, sd1_3_end, now):
        w.configure(text=jenjang[1])
    if time_in_range(sd4_6_start, sd4_6_end, now):
        w.configure(text=jenjang[2])
    if time_in_range(smp_start, smp_end, now):
        w.configure(text=jenjang[3])
    if time_in_range(sma_start, sma_end, now):
        w.configure(text=jenjang[4])

    root.after(60000, task)


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

root = Tk()
jenjang = ['PAUD', 'SD 1-3', 'SD 4-6', 'SMP', 'SMA']


end = datetime.time(1, 0, 0)
w = Label(root, text="PAUD", fg="red")
w.config(font='Helvetica 50 bold')

w.pack()
root.configure(background='black')
root.after(60000, task)
root.mainloop()