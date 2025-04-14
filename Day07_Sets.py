# Sets: Sets ek unordered collection hai jo unique items ko store krta hai. Ye mutable hote hain, lekin unme duplicate values nahi hoti. Sets ko curly braces ya set() function se create kiya jata hai.
# Sets ka use tab hota hai jab hume unique items ki zarurat hoti hai ya jab hume kisi collection me se duplicates ko remove karna hota hai.

sets = {1,2,3,4,5,4}
print(sets)  # ye {1, 2, 3, 4, 5} print karega kyunki sets me duplicate values nahi hoti
print(type(sets))  # ye <class 'set'> print karega
print(len(sets))  # ye 5 print karega kyunki sets me 5 unique items hain

# add and remove items in sets
sets.add(6)  # ye 6 ko set me add karega
print(sets) # ye {1, 2, 3, 4, 5, 6} print karega
sets.remove(3) # ye 3 ko set se remove karega
print(sets)  # ye {1, 2, 4, 5, 6} print karega

sets.pop()  # ye set se random item ko remove karega
sets.pop()  # ye set se random item ko remove karega
# print(sets)  # ye set ko print karega

# Sets me indexing nahi hoti
# print(numbers[0])  # ❌ Error

s = set()
print(s)  # ye empty set print karega
print(type(s))  # ye <class 'set'> print karega
s.add(1)  # ye 1 ko set me add karega
s.add(2)  # ye 2 ko set me add karega
print(s)
print(s.clear())  # ye set ko clear karega aur empty set return karega