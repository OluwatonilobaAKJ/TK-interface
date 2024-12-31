import tkinter as tk
import math

def cal_area(rad):
    area = round(math.pi*(rad**2),2)
    return area

def main():
    entered_radius = entry_box.get()

    try:
        radius = float(entered_radius)
    except ValueError:
        textbox["text"] = "Incorrect Value Entered"
        return
    
    x = format(cal_area(radius), '.2f')
    textbox["text"] = x + "mm"


window = tk.Tk()
window.geometry("400x210")
window.title("Area Of A Circle")
#
label = tk.Label(text = "Enter the radius:")
label.place(x = 10, y = 20, height = 25)
label.config(bg="lightblue", padx=0)
#
entry_box = tk.Entry(text = "")
entry_box.place(x= 10, y= 40, width= 110, height= 25)
#
button = tk.Button(text = "Calculate The Area", command = main)
button.config(font= "16")
button.place(x= 10, y= 170, width= 380, height= 35)
#
label2 = tk.Label(text= "The Area of the Circle is:")
label2.place(x= 140, y= 20)
label2.config(bg= 'lightblue', padx= 0)
textbox = tk.Message(text= "0.00mm", width= 200, font= "16")
textbox.config(bg= 'lightblue', padx= 0)
textbox.place(x= 140, y= 40)


window.mainloop() 