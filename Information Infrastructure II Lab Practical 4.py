from Tkinter import *



class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        #title and name entry
        Label(self, text="Calculate Your Airfare:").grid(row=0, column=0, columnspan=3)
        Label(self, text="Customer Name:").grid(row=1, column=0, sticky=E)
        self.name = Entry(self, width=25)
        self.name.grid(row=1, column=1, columnspan=2, sticky=W)

        Label(self, text="Select Your Options:").grid(row=2, column=0, columnspan=3)

        #class options
        Label(self, text="Choose Class:").grid(row=3, column=0)
        self.class_choice = StringVar()
        self.class_choice.set(None)
        Radiobutton(self, text = "Economy (baseline)", variable = self.class_choice, value = "an economy").grid(row=4, column=0)
        Radiobutton(self, text = "Business (50% more)", variable = self.class_choice, value = "a business").grid(row=5, column=0)
        Radiobutton(self, text = "Luxury (200% more)", variable = self.class_choice, value = "a luxury").grid(row=6, column=0)

        #airline options
        Label(self, text="Choose Airline:").grid(row=3, column = 1)
        self.airline = StringVar()
        self.airline.set(None)
        Radiobutton(self, text = "Delta (1 dollar per mile)", variable = self.airline, value = "Delta").grid(row=4, column=1)
        Radiobutton(self, text = "United (80 cents per mile)", variable = self.airline, value = "United").grid(row=5, column=1)
        Radiobutton(self, text = "Southwest (60 cents per mile)", variable = self.airline, value = "Southwest").grid(row=6, column=1)
        Radiobutton(self, text = "JetBlue (50 cents per mile)", variable = self.airline, value = "JetBlue").grid(row=7, column=1)

        #extras options
        Label(self, text="Inflight Extras:").grid(row=3, column=2)
        self.headphones = BooleanVar()
        Checkbutton(self, text="Headphones ($4)", variable = self.headphones).grid(row=4, column=2)
        self.beverage = BooleanVar()
        Checkbutton(self, text="Beverage ($10)", variable = self.beverage).grid(row=5, column=2)
        self.peanuts = BooleanVar()
        Checkbutton(self, text="Peanuts ($50)", variable = self.peanuts).grid(row=6, column=2)

        #distance traveled label and entry
        Label(self, text="Distance Traveled (miles):").grid(row=8, column=0)
        self.distance = Entry(self, width=15)
        self.distance.grid(row=9, column=0)

        #runs update_text to create the message
        Button(self, text= "Calculate!", command = self.update_text).grid(row=9, column=2)

        self.results = Text(self, width = 85, height = 6, wrap = WORD)
        self.results.grid(row=10, column=0, columnspan = 3)

    #creates the message the user sees        
    def update_text(self):
        message = "Thanks for flying with us, " + self.name.get() + ".\n"
        message += "You've selected " + self.class_choice.get()
        message += " class flight on " + self.airline.get() + " airlines"

        extras = []

        if self.headphones.get():
            extras.append(" headphones")
        if self.beverage.get():
            extras.append(" a beverage")
        if self.peanuts.get():
            extras.append(" peanuts")
        if extras:
            message += " with"

        message += ",".join(extras)
        message += "."

        total = 0

        #accounts for price difference due to airline
        if self.airline.get() == "Delta":
            total = float(self.distance.get())
        if self.airline.get() == "United":
            total = float(self.distance.get())*.8
        if self.airline.get() == "Southwest":
            total = float(self.distance.get())*.6
        if self.airline.get() == "JetBlue":
            total = float(self.distance.get())*.5

        #accounts for price difference due to class
        if self.class_choice.get() == "a business":
            total = float(total)*1.5
        if self.class_choice.get() == "a luxury":
            total = float(total)*3

        #accounts for extras
        if self.headphones.get():
            total += 4
        if self.beverage.get():
            total += 10
        if self.peanuts.get():
            total += 50

        message += "\nYour total comes to $" + str("%0.2f" % total) + "."

        #calculates fees per full 100 miles
        fees = (int(self.distance.get())/100)*20

        #adds sales tax
        taxed_total = (total*1.07) + fees
        
        message += "\nWith 7% tax plus $" + str(fees) + " in fees "
        message += "your true final cost will be $" + str(round(taxed_total, 2))

        #clears message box and inserts new message
        self.results.delete(0.0, END)
        self.results.insert(0.0, message)
        

#main
root = Tk()
root.title("Airfare Estimator")
root.resizable(width = FALSE, height = FALSE)
app = Application(root)
root.mainloop()


