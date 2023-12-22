from tkinter import *

root = Tk()
root.title("SALES APPLICATION")
root.geometry("400x400")

Month_values = Label(root)
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", 
         "October", "November", "December")
Month_values["text"] = "Month : " + str(month)
Month_values.place(relx= 0.5, rely= 0.2, anchor=CENTER)


Profit_values = Label(root)
profits = (20000,45000,78000,134000,23500,456000,10980,345670,21200,123000,126700,97600)
Profit_values["text"] = "Profits : " + str(profits)
Profit_values.place(relx= 0.5, rely= 0.3, anchor=CENTER)


max_profit = Label(root)
min_profit = Label(root)


max_profit.place(relx= 0.5, rely= 0.5, anchor=CENTER)
min_profit.place(relx= 0.5, rely= 0.7, anchor=CENTER)
def maximum_profit():
    max_profit1 = max(profits)
    max_profit_index = profits.index(max_profit1)

    max_profit_month = month[max_profit_index]
    max_profit["text"] = "The maximum profit of " + str(max_profit1)+ " was recorded in the month of "+ str(max_profit_month)
    
def minimum_profit():
    min_profit1 = min(profits)
    min_profit_index = profits.index(min_profit1)

    min_profit_month = month[min_profit_index]
    min_profit["text"] = "The minimum profit of " + str(min_profit1)+ " was recorded in the month of "+ str(min_profit_month)

btn = Button(root, text = "Show Max Profiable Month", command=maximum_profit, bg = "blue", fg = "white")
btn.place(relx= 0.5, rely= 0.4, anchor=CENTER)


btn1 = Button(root, text = "Show Min Profiable Month", command=minimum_profit, bg = "blue", fg = "white")
btn1.place(relx= 0.5, rely= 0.6, anchor=CENTER)


root.mainloop()

