""" Where's My Mouse? """
import tkinter

def mouse_click(event):

    # retrieve XY coords as a tuple
    coords = root.winfo_pointerxy()
    # tuples are immutable
    print('coords: {}'.format(coords))
    print('X: {}'.format(coords[0]))
    print('Y: {}'.format(coords[1]))

root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()
