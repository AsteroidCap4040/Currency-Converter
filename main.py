#Import Libraries
import tkinter
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from data import countries, money_country_data

#Constants
IMAGE = Image.open("C:\\Users\\pvdev\\OneDrive\\Desktop\\git_demo\\Currency-Converter\\swap.png")
BACKGROUND_COLOR = "#FFF5E1"
SWAP_BUTTON_COLOR = "#FF953E"
CALCULATE_BUTTON_COLOR = "#0C1844"

#Function to swap the countries
def swap():
    #Get the current value
    from_country = from_dropdown.get()
    to_country = to_dropdown.get()
    
    #Generating a error box if the fields are empty
    if from_country == "" or to_country == "":
        messagebox.showerror(title="Error !", message="Field is Empty")
    else:
        #Swapping values usinng a temporary variable
        temp = from_country
        from_country = to_country
        to_country = temp

        #Re-inserting the values
        from_dropdown.set(from_country)
        to_dropdown.set(to_country)

#Cobersion Function
def convert():
    from_country = from_dropdown.get() #Getting the 'from country' name/code
    to_country = to_dropdown.get() #Getting the 'to country' name/code

    #Generating a error box if the fields are empty
    if from_country == "" or to_country == "":
        messagebox.showerror(title="Error !", message="Field is Empty")
    else:
        money = from_country_input.get() #Getting the money input from the 'from country'

        #Generating a error box if the fields are empty or non numerical
        if money == "" or not money.replace('.', '', 1).isdigit() :
            messagebox.showerror(title="Error !", message="Enter a valid amount")
        else:
            money = float(money) #Converting it to a float value

            #Giving a error if the entered value is negative
            if money < 0:
                messagebox.showerror(title="Error !", message="Amount can't be negative")
            else:
                #The Base of the currencies is based on USD
                divisor = money_country_data[from_country]["value"]
                multiplier = money_country_data[to_country]["value"]

                converted_money = (money/divisor)*multiplier

                to_country_input.delete(0, tkinter.END) #Removing if there is any existing value 
                to_country_input.insert(0, str(converted_money)) #Inserting the calculated value

#Creating the screen
window = tkinter.Tk()
window.title("Currency Converter")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=10)

#From COuntry Fields
#Money Input
from_country_input = tkinter.Entry()
from_country_input.config(font=("Ariel", 15))
from_country_input.grid(column=0, row=1, padx=20, pady=20)

#Country Selection
from_dropdown = ttk.Combobox(values=countries)
from_dropdown.config(font=("Ariel", 15))
from_dropdown.grid(column=2, row=1)

#Swap button
swap_image = ImageTk.PhotoImage(IMAGE)
swap_button = tkinter.Button(image=swap_image, command=swap, bg=SWAP_BUTTON_COLOR)
swap_button.grid(column=1, row=2)

#Tpo COuntry Fields
#Money Input
to_country_input = tkinter.Entry()
to_country_input.config(font=("Ariel", 15))
to_country_input.grid(column=0, row=3, padx=20, pady=20)

#Country Selection
to_dropdown = ttk.Combobox(values=countries)
to_dropdown.config(font=("Ariel", 15))
to_dropdown.grid(column=2, row=3)

#Calculate button
calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.config(bg=CALCULATE_BUTTON_COLOR, fg="white", font=("Ariel", 15, "bold"))
calculate_button.grid(column=1, row=4)

#Exit loop
window.mainloop()