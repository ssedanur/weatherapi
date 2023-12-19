#import libraries

import tkinter as tk
import requests

#from PIL import Image


def getWeather(root):

    city = textField.get()
    #text entered by the user is taken and assigned to the city variable

    api = "http://api.weatherapi.com/v1/current.json?key=#add key number + city + "&aqi=no"
    #http request
    

    json_data = requests.get(api).json()
 
    conditiondata = json_data['current']['condition']['text']
    tempc = float(json_data['current']['temp_c'])
    feelslikec = float(json_data['current']['feelslike_c'])


    final_info = conditiondata + "\n" + str(tempc) + "°C" 
    final_data = "\n" + "Feels Like: " + str(feelslikec) + "°C"
    
    
    
    label3.config(text = final_info)
    label4.config(text = final_data)

    
root = tk.Tk()
root.geometry("700x500")
root.title("Weather App")

root.resizable(False,False)

search_img = tk.PhotoImage(file ="#add file path for search image")
myimg = tk.Label(image= search_img)
myimg.place(x=20,y=20)

textField = tk.Entry(root, justify='center', width = 17, font = ("poppins",25,"bold"),bg = "#404040",border= 0,fg="white")
textField.place(x=80,y=40)

textField.focus()
textField.bind('<Return>', getWeather)
#<Return>= enter

#edit_img = tk.Image.open("#add file path for resize image")
#new_logo = edit_img.resize((150,150))
#new_logo.save('new_logo_150.png')

logo_img = tk.PhotoImage(file ="add file path for logo")
logo=tk.Label(image = logo_img)
logo.place(x=150,y=100)


label1 = tk.Label(root,text = "Weather: ",font = ("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=350,y=130)
label2 = tk.Label(root,text = "Feels Like: ",font = ("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=350,y=180)


label3= tk.Label(root)
label4=tk.Label(root)

label3.place(x=450,y=130)
label4.place(x=490,y=170)


root.mainloop()
