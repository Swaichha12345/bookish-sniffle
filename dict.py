# dic={'code':"price",'121':"Rs 1000"}
# # print(dic['code'])
# # print(dic.get('code'))
# # print(dic.values())
# # print(dic.keys())
# # print(dic['121'])
# for key in dic:
#     print(key,dic[key])
    
# emp1={1:11,2:90,3:100}
# dic.update(emp1)
# print(dic)
# dic.pop(1)    
# # dic.clear()  # clear the dictionary
# print(dic)
# dic.popitem()  # remove the last inserted item
# print(dic)
# del dic['code']  # delete the key 121
# print(dic)


names={1:"Avinash",2:"Deepak",3:"Daksh",4:"Swaichha"}
print(names)
print(names[1])
print(names.get(1))
print(names.keys())
print(names.values())
for key in names.keys():
    print(f"roll no of {names[key]} is {key}")
    
cities = {
    "Delhi": 19000000,
    "Mumbai": 20400000,
    "Bangalore": 12000000
}

print(cities["Delhi"])    
# print(cities.get("Delhi"))
print(cities.keys()) 
cities["Chennai"] = 909090  # Add element using square brackets
cities["Gorakhpur"]=101010101
print(cities)
cities.update({"Gorakhpur": 22})  # Update using dictionary syntax
cities.update({"Gorakhpur":222})
print(cities)
cities.pop("Mumbai")
print((cities))
for key in cities.keys():
    print(f"Ppopulation of {key} is {cities[key]}")
    
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict1.update(dict2)    
# print(dict1)


# val=input("Enter a value")
# char_freq={}
# for char in val:
#     if char in char_freq:
#         char_freq[char] +=1
#     else:
#         char_freq[char] = 1    
        
# for key, value in char_freq.items():
#     print(f"Character {key} occurs {value} times")        
    
# invert dict in the same dictionary - Method 1: Using list() to create a snapshot
print("Before inversion:", cities)
for key, value in list(cities.items()):  # list() creates a snapshot of items
    # What does "snapshot" mean?
    # cities.items() returns a dynamic view that changes when the dict changes
    # list(cities.items()) creates a fixed copy of all key-value pairs at this moment
    # This prevents "dictionary changed size during iteration" error
    cities[value] = key
    del cities[key]  # Remove the original key
print("After inversion:", cities)

# Alternative Method 2: Store items first, then clear and rebuild
# items_snapshot = list(cities.items())
# cities.clear()
# for key, value in items_snapshot:
#     cities[value] = key
# print("Method 2 result:", cities)     