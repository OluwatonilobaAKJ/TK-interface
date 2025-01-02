import tkinter as tk

def check_course_eligibility():
    try:
        age = int(entry_box.get())
        required_age = 18

        if age >= required_age and age < 60:
            result = "You can start the course now"
            if age == 30:
                result = "You are very eligible for a discount on courses"
        elif age >= 60:
            result = "You are eligible for a discount on courses"
        else:
            years_to_go = required_age - age
            result = f"Sorry, you have {years_to_go} more years to wait."

        # Display result in the TextBox
        textbox["text"] = result
    except ValueError:
        textbox["text"] = "Incorrect Value Entered"


# Tkinter Window Application
window = tk.Tk()
window.geometry("400x210")
window.title("Course Eligibility")
#
label = tk.Label(text = "Enter your age:")
label.place(x = 10, y = 20, height = 25)
label.config(bg="lightblue", padx=0)
#
entry_box = tk.Entry(text = "")
entry_box.place(x= 10, y= 40, width= 110, height= 25)
#
button = tk.Button(text = "Check Eligibilty", command = check_course_eligibility)
button.config(font= "16")
button.place(x= 10, y= 170, width= 380, height= 35)
#
label2 = tk.Label(text= "Results:")
label2.place(x= 140, y= 20)
label2.config(bg= 'lightblue', padx= 0)
#
textbox = tk.Message(text= "-----", width= 200, font= "16")
textbox.config(bg= 'lightblue', padx= 0)
textbox.place(x= 140, y= 40)


window.mainloop() 