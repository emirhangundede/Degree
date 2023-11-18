from tkinter import *

screen = Tk()
screen.title("Degree")
screen.minsize(height=200,width=300)
screen.maxsize(height=200,width=300)

degreeLabel = Label(text="Entry Degree", font=100)
degreeLabel.pack()

degreeEntry = Entry()
degreeEntry.pack()

def celsiustofahrenheit():
    celsius = float(degreeEntry.get())
    fahrenheit = (celsius * 1.8) + 32
    resultLabel.config(text=f"{celsius} degree celsius equal {fahrenheit} fahrenheit")

def fahrenheittoCelsius():
    fahrenheit = float(degreeEntry.get())
    celsius = (fahrenheit - 32) / 1.8
    resultLabel.config(text=f"{fahrenheit} degree fahrenheit equal {celsius} celsius")

def celsiustokelvin():
    celsius= float(degreeEntry.get())
    kelvin = celsius+273.15
    resultLabel.config(text=f"{celsius} degree celsius equal {kelvin} kelvin")

def kelvintocelsius():
    kelvin= float(degreeEntry.get())
    celsius = kelvin-273.15
    resultLabel.config(text=f"{kelvin} degree kelvin equal {celsius} celsius")





cltofaButton = Button(text="CelsiusToFahrenheit", command=celsiustofahrenheit)
cltofaButton.pack()

fatoclButton = Button(text="FahrenheitToCelsius", command=fahrenheittoCelsius)
fatoclButton.pack()

cltokelButton = Button(text="CelsiusToKelvin", command=celsiustokelvin)
cltokelButton.pack()

keltoclButton = Button(text="KelvinToCelsius", command=kelvintocelsius)
keltoclButton.pack()

resultLabel = Label()
resultLabel.pack()

mainloop()