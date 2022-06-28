temperature = 75

if temperature > 80:
    print("It's too hot!")
    print("Stay inside and hidritaded")
elif temperature < 60:
    print("Stay inside and hidritaded")
else:    
    print("Go out!")

temperature = 50

if temperature > 80 or temperature < 60:
    print("Stay inside and hidritaded")
else:
    print("Enjoy the outdoors")


temperature = 75
forecast = "rain"

if temperature > 80 and forecast != "rain":
    print("Go out!")
else:
    print("Stay inside!")

forecast = "sunny"

if not forecast == "sunny":
    print("Go out")
else:
    print("Stay inside!")