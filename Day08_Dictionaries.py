# Dictionary: Dictionary ek colletctio hoti hai jo key value pair me store hoti hai 
# Dictionary ko curly braces ya dict() function se create kiya jata hai.
# Dictionary ka use tab hota hai jab hume kisi item ko uniquely identify karna ho ya jab hume kisi collection me se kisi item ko search karna ho.

student = {
    "name": "Urooj",
    "age": 21,
    "qualification": "Software Engineer",
    "skills": ["Python", "Java", "C++"]
}

print(student)  # ye dictionary ko print karega
print(student["name"])  # ye name ko access karega
 
print(student.items())  # ye dictionary ke items ko access karega
print(student.keys())  # ye dictionary ke keys ko access karega
print(student.values())  # ye dictionary ke values ko access karega

# change value of item at specific key
student["age"] = 22  # ye age ko change karega
print(student)

#update value of item at specific key
student.update({"name": "Urooj Islam","surname":"Pathan"})  # ye name ko update karega or surname phele se nhi hai to usse add krdega
print(student)


# new key value pair add krne k liye
student["city"] = "Karachi"  # ye city ko add karega
print(student) # ye dictionary ko print karega

print(student.get("name"))  # ye name ko access karega
print(student["name"])
# both give same output if value is available in dictionary otherwise .get() give none in output but index[name] gives error

value = student.pop("age")  # ye age ko remove karega or value ko return karega
print(value)  # ye age ko print karega

item = student.popitem()  # ye last item ko remove karega or value ko return karega in form of tuple
print(item)  # ye last item ko print karega
print(student)
