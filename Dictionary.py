vehicle={"sport":"Mustang", "city":"Aviator", "off-road":"Bronco", "truck":"F-150", "street":"Expedition", "utility":"Ranger"}

print("Entry the car category you want, then you will have the Ford related car")
car=input()

car=car.lower()

selected=vehicle.get(car,"The search didin't find the car category you selected")

print(selected)