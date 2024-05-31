# emoji print 
def weather_to_emoji(weather:str) ->None:
    if weather =="rain":
        print("🌧️")
    elif weather =="cloudy":
        print("☁️")
    elif weather =="thunderstorm":
        print("⛈️")
    else:
        print("😎")

weather_to_emoji("wind")                    



#lists
fruit=['🍌','🍎',"🟠",'🍇']
fruit.append("🍓")
for fur in enumerate(fruit):
    print(f'fruit :{fur[1]}  {fur[0]}')



 
