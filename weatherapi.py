
#request python kullanarak http istekleri gönderir
#tkinter grafiksel kullanıcı arayüzü aracı

#import libraries

import tkinter as tk
import requests

#from PIL import Image
#icon boyutu ayarlamak için dahil ettik


#fonksiyon oluşturuyoruz


def getWeather(root):

    city = textField.get()


    #bir metin giriş alanından kullanıcının girdiği metni almak için kullanılır
    #entry widgeti için get() yöntemini kullanarak kullanıcının girdiği metin alınır ve şehir değişkenine atanır

    api = "http://api.weatherapi.com/v1/current.json?key=74345ffbfe1444fdb1a154413230210&q=" + city + "&aqi=no"
    #bir hava durumu api sine http isteği yapıyoruz

    json_data = requests.get(api).json()
    #http get isteği gönderir ve api ye erişip verileri çeker 
    #ardından bu verileri python veri yapısı olan json(javascript object notation) formatında işler


    conditiondata = json_data['current']['condition']['text']
    tempc = float(json_data['current']['temp_c'])
    feelslikec = float(json_data['current']['feelslike_c'])
    #json verisinden hava durumu bilgilerini çektik
    

    final_info = conditiondata + "\n" + str(tempc) + "°C" 
    final_data = "\n" + "Feels Like: " + str(feelslikec) + "°C"
    
    
    
    label3.config(text = final_info)
    label4.config(text = final_data)
    #sanırım etiket mantığı dinamik olarak değişim sağlıyor
    

root = tk.Tk()
root.geometry("700x500")
root.title("Weather App")

root.resizable(False,False)

search_img = tk.PhotoImage(file ="/home/sseda/weather_api/search_copy.png")
myimg = tk.Label(image= search_img)
myimg.place(x=20,y=20)

textField = tk.Entry(root, justify='center', width = 17, font = ("poppins",25,"bold"),bg = "#404040",border= 0,fg="white")
textField.place(x=80,y=40)

textField.focus()
textField.bind('<Return>', getWeather)
#return klavye tuşunun enter tuşunu temsil eder yani o tuşa basınca belirli bir işlem gerçekleşir o da getWeather

#edit_img = tk.Image.open("/home/sseda/weather_api/logo1.png")
#new_logo = edit_img.resize((150,150))
#new_logo.save('new_logo_150.png')

logo_img = tk.PhotoImage(file ="/home/sseda/new_logo_150.png")
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