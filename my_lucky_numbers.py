from random import choice
from lexarithmoi import *
from tkinter import *
from datetime import date
import os

list = []
list_of_available = [*range(1, 46, 1)]

random_nums = []
random_nums_tzoker = []

list_tzoker = []
list_tzoker_available = [*range(1, 21, 1)]

total_days_born = 0

number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
print(f"number 1 is: {number1}")


def first_number():
    word = entry1.get()
    if word != "" and word != 0:
        onoma1 = split(word)
        sum = wordnums(onoma1)
        num1 = sum
        global number1
        number1 += num1
        #print(num1)
        num1 = num1 % 46
        if num1 == 0:
            num1 = choice(list_of_available)
            random_nums.append(num1)
        #print(num1)
        if 0 < num1 <= 45 and int(num1) not in list:
            list.append(num1)
            list_of_available.remove(num1)
        else:
            if num1 != 0:
                num1 = choice(list_of_available)
                random_nums.append(num1)
                list.append(num1)
                list_of_available.remove(num1)
            else:
                print("Zero(1)!!!")
        return num1


def second_number():
    word2 = entry2.get()
    if word2 != "":
        onoma2 = split(word2)
        sum = wordnums(onoma2)
        num2 = sum
        global number2
        number2 += num2
        #print(num2)
        num2 = num2 % 46
        if num2 == 0:
            num2 = choice(list_of_available)
            random_nums.append(num2)
        #print(num2)
        if 0 < num2 <= 45 and int(num2) not in list:
            list.append(num2)
            list_of_available.remove(num2)
        else:
            if num2 != 0:
                num2 = choice(list_of_available)
                random_nums.append(num2)
                list.append(num2)
                list_of_available.remove(num2)
            else:
                print("Zero(2)!!!")


def third_number():
    num3 = entry3.get()
    if num3 != "" and num3 != 0:
        global number3
        number3 += int(num3)
        if 0 < int(num3) <= 45 and int(num3) not in list:
            list.append(int(num3))
            list_of_available.remove(int(num3))
        else:
            num3 = choice(list_of_available)
            random_nums.append(num3)
            list.append(num3)
            list_of_available.remove(num3)


def forth_number():
    num4 = entry4.get()
    if num4 != "" and num4 != 0:
        global number4
        number4 += int(num4)
        if 0 < int(num4) <= 45 and int(num4) not in list:
            list.append(int(num4))
            list_of_available.remove(int(num4))
        else:
            num4 = choice(list_of_available)
            random_nums.append(num4)
            list.append(num4)
            list_of_available.remove(num4)


def fifth_number():
    num5 = entry5.get()
    if num5 != "" and num5 != 0:
        global number5
        number5 += int(num5)
        num5 = int(num5)
        num5 = num5 % 46
        if num5 == 0:
            num5 = choice(list_of_available)
            random_nums.append(num5)
        if 0 < int(num5) <= 45 and int(num5) not in list:
            list.append(int(num5))
            list_of_available.remove(int(num5))
        else:
            num5 = choice(list_of_available)
            random_nums.append(num5)
            list.append(num5)
            list_of_available.remove(num5)


def tzoker_number(num1, num2, num3, num4, num5):
    tzoker = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
    if tzoker != "" and tzoker != 0:
        tzoker = tzoker % 21
        list_tzoker.append(tzoker)
        print(f"Tzoker is number: {tzoker}")
        print(list_tzoker)
    if 0 in list_tzoker:
        list_tzoker.remove(0)
        tzoker2 = choice(list_tzoker_available)
        random_nums_tzoker.append(tzoker2)
        list_tzoker.append(tzoker2)
        list_tzoker_available.remove(tzoker2)


def days_calculation():
    today = date.today()
    day = entry3.get()
    month = entry4.get()
    year = entry5.get()
    if day != "" and month != "" and year != "":
        born = date(int(year), int(month), int(day))
        days_born = today - born
        global total_days_born
        total_days_born += days_born.days
        return days_born


def reset():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    global list
    list = []
    global list_of_available
    list_of_available = [*range(1, 46, 1)]
    global list_tzoker
    list_tzoker = []
    global list_tzoker_available
    list_tzoker_available = [*range(1, 21, 1)]
    global total_days_born
    total_days_born = 0
    global number1
    number1 = 0
    global number2
    number2 = 0
    global number3
    number3 = 0
    global number4
    number4 = 0
    global number5
    number5 = 0
    label_main1["text"] = f"Βρες τους τυχερούς σου αριθμούς Τζόκερ συμπληρώνοντας\n\n " \
                          f"τα κενά και πατώντας 'Καταχώρηση'.\n\n" \
                          f"Πάτα το Reset κάτω δεξιά για να κάνεις νέα καταχώρηση.\n\n" \
                          f"Πάτησε το Print για να εκτυπώσεις τα νούμερα σου σε ένα αρχείο."


def print_to_file():
    try:
        username = os.getlogin()  # Fetch username
        file = open(f'C:\\Users\\{username}\\Desktop\\My_lucky_numbers.txt', 'w')
        file.write(label_main1["text"])
        file.close()
        label_main1["text"] = f"Τα τυχερά σου νούμερα εχουν εκτυπωθεί σε ένα txt αρχείο \n\nστην επιφάνεια εργασίας"
    except:
        label_main1["text"] = f"Τα τυχερά νούμερα δεν μπορούν να εκτυπωθούν σε αυτό τον υπολογιστή"


def about():
    os.startfile("about_tzoker.txt")


def main():
    first_number()
    second_number()
    third_number()
    forth_number()
    fifth_number()
    tzoker_number(num1=number1, num2=number2, num3=number3, num4=number4, num5=number5)
    days_calculation()
    name = entry1.get()
    if name != "":
        label_main1["text"] = f"{name[0:-1] if name[-1] == 'ς' else name} γεννήθηκες στις {entry3.get()} / " \
                              f"{entry4.get()} του {entry5.get()} πριν απο ακριβώς {total_days_born:,} ημέρες\n\n" \
                              f"Το όνομα σου αντιστοιχεί στον αριθμό {number1:,} και το επίθετο σου στον αριθμό {number2:,}\n\n" \
                              f"Οι προσωπικοί σου τυχεροί αριθμοί είναι οι: {sorted(list)}\n\n" \
                              f"και Τζόκερ ο αριθμός {list_tzoker[0]}\n\n" \
                              f"Είθε να σου φέρουν καλή τύχη και μην ξεχνάς να παίζεις Τζόκερ!!..."


window = Tk()
window.geometry("800x550")
window.wm_iconbitmap("icon.ico")
image = "12-1a.png"
filename = PhotoImage(file = image)
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.title("My Lucky Numbers")

label1 = Label(text="Ατομικά Στοιχεία", bg="RoyalBlue1", borderwidth=4, relief="raised")
label1.place(x=100, y=60, width=200, height=30)
label1.config(font='Helvetica 12 bold', foreground="white")

label2 = Label(text="Όνομα", bg="SteelBlue1", borderwidth=2, relief="raised")
label2.place(x=75, y=100, width=100, height=25)
label2.config(font='Helvetica 12 bold', foreground="white")

label3 = Label(text="Επίθετο", bg="SteelBlue1", borderwidth=2, relief="raised")
label3.place(x=215, y=100, width=100, height=25)
label3.config(font='Helvetica 12 bold', foreground="white")

label4 = Label(text="Ημερομηνία Γέννησης", bg="RoyalBlue1", borderwidth=4, relief="raised")
label4.place(x=400, y=60, width=200, height=30)
label4.config(font='Helvetica 12 bold', foreground="white")

label5 = Label(text="Ημέρα", bg="SteelBlue1", borderwidth=2, relief="raised")
label5.place(x=395, y=100, width=60, height=25)
label5.config(font='Helvetica 12 bold', foreground="white")

label6 = Label(text="Μήνας", bg="SteelBlue1", borderwidth=2, relief="raised")
label6.place(x=470, y=100, width=60, height=25)
label6.config(font='Helvetica 12 bold', foreground="white")

label7 = Label(text="Έτος", bg="SteelBlue1", borderwidth=2, relief="raised")
label7.place(x=545, y=100, width=60, height=25)
label7.config(font='Helvetica 12 bold', foreground="white")

label_main1 = Label(text="Βρες τους τυχερούς σου αριθμούς Τζόκερ συμπληρώνοντας\n\n τα κενά"
                         " και πατώντας 'Καταχώρηση'.\n\n"
                         "Πάτα το Reset κάτω δεξιά για να κάνεις νέα καταχώρηση.\n\n"
                         "Πάτησε το Print για να εκτυπώσεις τα νούμερα σου σε ένα αρχείο.",
                    bg="white", fg="blue", bd=5, justify=CENTER, borderwidth=5, relief="sunken")
label_main1.place(x=80, y=210, width=640, height=230)
label_main1.config(font='Helvetica 12 bold', foreground="black")

entry1 = Entry(text="", font=12, bd=3, justify=CENTER, highlightbackground="#37d3ff")
entry1.place(x=60, y=130, width=130, height=30)

entry2 = Entry(text="", font=12, bd=3, justify=CENTER)
entry2.place(x=200, y=130, width=130, height=30)

entry3 = Entry(text="", font=12, bd=3, justify=CENTER)
entry3.place(x=395, y=130, width=60, height=30)

entry4 = Entry(text="", font=12, bd=3, justify=CENTER)
entry4.place(x=470, y=130, width=60, height=30)

entry5 = Entry(text="", font=12, bd=3, justify=CENTER)
entry5.place(x=545, y=130, width=60, height=30)

button1 = Button(text="Καταχώρηση", command=main, bd=10)
button1.place(x=630, y=60, width=150, height=100)
button1.config(font='Helvetica 12 bold', foreground="black")

button2 = Button(text="Reset", command=reset, bd=8)
button2.place(x=715, y=470, width=70, height=50)
button2.config(font='Helvetica 10 bold', foreground="black")

button3 = Button(text="Print", command=print_to_file, bd=8)
button3.place(x=615, y=470, width=70, height=50)
button3.config(font='Helvetica 10 bold', foreground="black")

button4 = Button(text="About", bd=6, command=about)
button4.place(x=720, y=15, width=60, height=30)
button4.config(font='Helvetica 10 bold', foreground="black")

main()

window.mainloop()

print(list)
print(sorted(list))
print(list_of_available)
print(list_tzoker)
print(list_tzoker_available)
print(f"number 1 is: {number1}")
print(f"number 2 is: {number2}")
print(f"number 3 is: {number3}")
print(f"number 4 is: {number4}")
print(f"number 5 is: {number5}")
print(f"tzoker number is: {list_tzoker}")
print(f"Random numbers: {random_nums}")
print(f"Random tzoker numbers: {random_nums_tzoker}")