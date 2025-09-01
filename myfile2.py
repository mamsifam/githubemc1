import tkinter as tk

window =tk.Tk()
window.title('git hub test window')
label = tk.Label(window,text='Devalop')
label.pack(padx=10,pady=10)
label2 = tk.Label(window,text='Devalop2')
label2.pack(padx=15,pady=15)
button = tk.button(window,text ='click here')
button.pack()

window.mainloop()
