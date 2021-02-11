import tkinter

# perlu di ingat, setiap class di dalam python itu selalu di awali dengan huruf besar
main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = 'Label1')
label2 = tkinter.Label(main_window, text = 'Label2')

tombol1 = tkinter.Button(main_window, text = 'tombol1')
tombol2 = tkinter.Button(main_window, text = 'tombol2')

# lalu jika method atau fungsi tidak di awali dengan huruf besar
# Method Positioning
label1.pack()
label2.pack()

tombol1.pack()
tombol2.pack()

# Method menampilkan GUI
main_window.mainloop()