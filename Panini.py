plan=["sleeping", "eating", "coding", "gaming", "reading"]
print(plan[0])
print(plan[-1])
print(plan[1:4])
print(plan[-1: :-1])
plan[1] = "exercising"
print(plan)
plan.append("meeting")
plan.insert(0,"walking")
plan.remove("gaming")
weekend_activity_2=[]
weekend_activity_2.extend(plan)
print(weekend_activity_2)

city=("poznan","poland",52.41,16.93)
print(city[1])
print(city[-1])
print(type(city))
urban,nation,latitude,longitude=city
print(urban)
print(nation)

