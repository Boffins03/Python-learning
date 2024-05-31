cities_F={'New York':32,"Los Angle":20,'chicago':25,'boston':30}
cities_c={key:round(((value-32)*(5/9))) for (key,value) in cities_F.items()}
print(cities_c)

cities_w={"Los angle":'sunny',"new york":'cloudy','boston':'wind','chicago':'sunny'}
sunny_cities={key:value for (key,value) in cities_w.items() if value=='sunny'}
print(sunny_cities)

cities_temp={'New York':32,"Los Angle":20,'chicago':25,'boston':30}
hot_cold={key:("warm" if value >=25 else "cold") for (key,value) in  cities_temp.items()}
print(hot_cold)
