import tkinter

window = tkinter.Tk()
window.title("BMI (Vücut Kitle Endeksi) Hesaplayıcı")
window.minsize(400, 350)



def click_button():
    try:
        kilo = float(my_entry2.get())
        boy = float(my_entry.get())/100
        bmi = kilo / (boy * boy)
        if bmi < 18.5:
            my_label3.config(text=f"BMI = {bmi:.2f} - Underweight")
        elif 18.5 <= bmi <= 24.9:
            my_label3.config(text=f"BMI = {bmi:.2f} - Normal")
        elif 25 <= bmi <= 29.9:
            my_label3.config(text=f"BMI = {bmi:.2f} - Overweight")
        elif 30 <= bmi <= 34.9:
            my_label3.config(text=f"BMI = {bmi:.2f} - Obese (Class 1)")
        elif 35 <= bmi <= 39.9:
            my_label3.config(text=f"BMI = {bmi:.2f} - Obese (Class 2)")
        elif bmi >= 40:
            my_label3.config(text=f"BMI = {bmi:.2f} - Morbid Obese (Class 3)")
    except:
        my_label3.config(text="Please enter a valid number!")




my_label = tkinter.Label(window, text="Enter Your Height (cm)")
my_label.config(font=("Arial", 20))
my_label.pack(pady=20)

my_entry = tkinter.Entry(width=20)
my_entry.pack(pady=10)

my_label2 = tkinter.Label(window, text="Enter Your Weight (cm)")
my_label2.config(font=("Arial", 20,))
my_label2.pack(pady=20)

my_entry2 = tkinter.Entry(width=20)
my_entry2.pack(pady=10)


my_label3 = tkinter.Label(window, text="")
my_label3.config(font=("Arial", 20,))
my_label3.pack(pady=20)



my_button = tkinter.Button(window, text="Calculate BMI", command=click_button)
my_button.pack(pady=10)



window.mainloop()