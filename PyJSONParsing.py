import json 
  
# Opening JSON file 
f = open('LoopedBackEmployees.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in data['LoopedBack_Employees']: 
    print(json.dumps(data, indent=1))
  
# Closing file 
f.close() 