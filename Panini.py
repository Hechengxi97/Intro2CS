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
weekend_activities_2=[]
weekend_activities_2.extend(plan)
print(weekend_activities_2)

