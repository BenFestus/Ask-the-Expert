'''Ask the Expert - Capital Countries'''

from tkinter import Tk, simpledialog, messagebox

#Function reads text from file
def read_from_file():
    #Opens text file
    with open('capital_data.txt') as file:
        for line in file:
            #Strip newline character from line
            line = line.strip('\n')
            #Split line and save word before and after '/' respectively in country and capital variable
            country, capital = line.split('/')
            #Append country and capital to 'the_world' dictionary
            the_world[country] = capital

def write_to_file(country, city):
    #Opens new text file
    with open('capital_data_append.txt', 'a') as file:
        #Write new country and capital to file
        file.write(country + '/' + city + '\n')

root = Tk()
root.withdraw()

print('Welcome to Ask the Expert - Capital cities of the World')

#Dictionary holding countries and capitals
the_world = {}
read_from_file() #Calling read from file function

while True:
    query_country = simpledialog.askstring('ASK!', 'Ask the name of any country and I\'ll tell you it\'s capital')
    #If query country is in the world dictionary
    if query_country in the_world:
        result = the_world[query_country] #Stores value gotten from dictionary
        messagebox.showinfo('I Know!', 'Capital of ' + query_country + ' is ' + result)
    #If query country is nor in dictionary
    else:
        try:
            new_city = simpledialog.askstring('Teach Me!', 'What is the capital city of ' + query_country + '?')
            the_world[query_country] = new_city #Append new city and query country to dictionary
            #Write new country and capital in new file for further evaluation
            write_to_file(query_country, new_city)
        except Exception as e:
            break

root.mainloop()
