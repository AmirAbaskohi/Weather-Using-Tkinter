import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def formatResponse(weather):
	try:
		name = weather['name']
		description = weather['weather'][0]['description']
		temp = weather['main']['temp']

		out = 'City: %s \nConditions: %s \n Tempreature (°F): %s' %(name, description, temp)
	except:
		out = 'The was a problem in retrieving that information ;('
	return out

def getWeather(city):
	weatheKey = '3be9b38f3078a7f09de8c91ea7e787ed'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weatheKey, 'q':city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	label['text'] = formatResponse(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


backgroundImage = tk.PhotoImage(file='images/landscape.png')
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lowerFrame = tk.Frame(root, bg='#80c1ff', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame)
label.place(relwidth=1, relheight=1)

root.mainloop()