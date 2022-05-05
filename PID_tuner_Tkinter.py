import tkinter as tk
from tkinter import ttk
import serial
import time
#stm32 = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# root window
root = tk.Tk()

root.geometry('1500x500')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value_p = tk.DoubleVar()
current_value_i = tk.DoubleVar()
current_value_d = tk.DoubleVar()

def get_current_value_p():
    return '{: .3f}'.format(current_value_p.get())
def get_current_value_i():
    return '{: .3f}'.format(current_value_i.get())
def get_current_value_d():
    return '{: .3f}'.format(current_value_d.get())

def slider_changed_p(event):
    value_label_p.configure(text=get_current_value_p())
def slider_changed_i(event):
    value_label_i.configure(text=get_current_value_i())
def slider_changed_d(event):
    value_label_d.configure(text=get_current_value_d())

# label for the slider
slider_label_p = ttk.Label(
    root,
    text='P degeri:'
)
slider_label_i = ttk.Label(
    root,
    text='i degeri:'
)
slider_label_d = ttk.Label(
    root,
    text='d degeri:'
)

"""slider_label_p.grid(
    column=0,
    row=1,
    sticky='w'
)
slider_label_i.grid(
    column=0,
    row=2,
    sticky='w'
)
slider_label_d.grid(
    column=0,
    row=3,
    sticky='w'
)"""
#  slider
slider_p = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed_p,
    variable=current_value_p
)
slider_i = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed_i,
    variable=current_value_i
)
slider_d = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed_d,
    variable=current_value_d
)

slider_p.grid(
    column=1,
    row=1,
    sticky='we'
)
slider_i.grid(
    column=1,
    row=2,
    sticky='we'
)
slider_d.grid(
    column=1,
    row=3,
    sticky='we'
)
# current value label
current_value_label_p = ttk.Label(
    root,
    text='P mevcut deger:'
)
current_value_label_i = ttk.Label(
    root,
    text='I mevcut deger:'
)
current_value_label_d = ttk.Label(
    root,
    text='D mevcut deger:'
)

current_value_label_p.grid(
    row=1,
    columnspan=1,
    sticky='n',
    ipadx=10,
    ipady=10
)
current_value_label_i.grid(
    row=2,
    columnspan=1,
    sticky='n',
    ipadx=10,
    ipady=10
)
current_value_label_d.grid(
    row=3,
    columnspan=1,
    sticky='n',
    ipadx=10,
    ipady=10
)
# value label
value_label_p = ttk.Label(
    root,
    text=get_current_value_p()
)
value_label_i = ttk.Label(
    root,
    text=get_current_value_i()
)
value_label_d = ttk.Label(
    root,
    text=get_current_value_d()
)

value_label_p.grid(
    row=2,
    column=0,
    sticky='n'
)
value_label_i.grid(
    row=3,
    column=0,
    sticky='n'
)
value_label_d.grid(
    row=4,
    column=0,
    sticky='n'
)

def arm_disarm():
    print("arm-disarm")
    time.sleep(1)

exit_button = ttk.Button(
    root,
    text='arm-disarm',
    command=arm_disarm
)

exit_button.grid(
    ipadx=5,
    ipady=5,
)
#stm32.write(bytes(x, 'utf-8'))
pid="$"+get_current_value_p()+","+get_current_value_i()+","+get_current_value_d()
print(pid)

while True:
    pid = "$" + get_current_value_p() + "," + get_current_value_i() + "," + get_current_value_d()
    print(pid)
    root.update()