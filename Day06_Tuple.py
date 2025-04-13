# Tuple: Tuple is a collection which is ordered and unchangebale. Allows duplicate members.
# Tuple ko round brackets () ya tuple() function se create kiya jata hai.
# Tuple ka use tab hota hai jab hume items ko order me store karna ho ya jab hume kisi collection me duplicates ki zarurat ho.
colors = ("red", "green", "blue", "purple", "violet")
print(colors)

a = colors.count("violet")  # ye count krega ki violet tuple me kitni baar aata hai
print(a)
b = colors.index("blue")  # ye index return krega ki green tuple me kis index pr hai
print(b)

# immutable hone ki wajah se tuple change nhi hoti 
# colors[1] = "yellow"  # ye error dega kyunki tuple change nhi hoti
# print(colors)

# tuple ko list me convert krne k liye list() function use hota hai
color_list = list(colors)
color_list[1] = "yellow"  # ye ab change ho jayegi kyunki ye list hai
colors = tuple(color_list) # ab ye dobara tuple me convert ho jayegi
print(colors)
print(colors[0])  # ye first item ko access krega


tuples = (1,2,3,4,5,6,7,8,9,10)
repeat = tuples * 3  # ye tuple ko 3 baar repeat krega
print(repeat)

print(len(tuples)) # ye tuple ki length return krega

sliced = tuples[1:4] # ye tuple ko slice krega 1 se 4 tk
print(sliced)  





