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
urban,country,latitude,longitude=city
print(urban)
print(country)
city_list=list(city)
city_list[1]="China"
city=tuple(city_list)
print(city)

mine={"pizza","taccos","ramen","salad","burgers"}
friend={"pizza","sushi","tacos", "pierogi","pasta"}
all=mine.union(friend)
print(all)
both=mine.intersection(friend)
print(both)
only_one=mine.difference(friend)
print(only_one)



word={"cat":"mao","dog":"gou","fish":"yu","pig":"zhu"}
print(word["cat"])
print(len(word))
word["bird"]="niao"
word["cat"]="miao"
print(word)
word.update({"tiger":"laohu","monkey":"houzi"})
print(word)
print(list(word.keys()))
print(list(word.values()))
print(list(word.items()))
