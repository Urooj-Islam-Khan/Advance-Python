# Lists: List ordered collection hoti hai kisi b datatype ki jo change ho skti hy and duplicate values allow krti hai.
# Lists ko square brackets [] ya list() function se create kiya jata hai.
# Lists ka use tab hota hai jab hume items ko order me store karna ho ya jab hume kisi collection me duplicates ki zarurat ho.
Syntax = []
fruits = ["apple", "banana", "coconut", "mango"]
print(fruits)

# to change value of item at specific value 
fruits[2] = "orange"  #ye coconut ki jaga orange place krdega
fruits[1:3] = ["kiwi", "peach"] # ye banana ki jaga kiwi and mango ki jaga peach place krdega

print(fruits)

# to find length of a lists
print(len(fruits))

# to add/remove item in a list 
fruits.append("watermelon")
print(fruits)

fruits.insert(2, "grape")  # ye grape ko 1st index pr place krega
print(fruits)

fruits.remove("apple")  # ye apple ko remove krega
print(fruits)

fruits.extend(["avacado"])  # ye avocado ko list me add krega
print(fruits)

# access items in list
print(fruits[0])  # ye first item ko access krega
print(fruits[-1])  # ye last item ko access krega

# ranges in list
print(fruits[1:3])  # ye 1 se 3 tk ki items ko access krega

# check if items exists in list
if "banana" in fruits:
    print("yes")

list = [2, 5, 1, 6, 3, 4] 

list.sort() # ye list ko sort krega
print(list)

list.reverse() # ye list ko reverse krega
print(list)

list.insert(2,7) # ye 2nd index pr 7 ko place krega
print(list)

list.pop(3) # ye 3rd index pr se item ko remove krega
print(list)