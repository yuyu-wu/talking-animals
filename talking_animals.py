# Default Parameter Exercise - Talking Animals
# Write a function called speak  that accepts a single parameter, animal.  

# If animal is "pig", it should return "oink". 
# If animal is "duck", it should return "quack".  
# If animal is "cat", it should return "meow"
# If animal is "dog", it should return "woof"
# If animal is anything else, it should return "?"
# If no animal is specified, it should default to "dog"

# Use a large if-elif-else statement:
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"
    
    
# Use a dictionary that maps animal names to noises.
noises = {
    "dog": "woof", 
    "pig": "oink", 
    "duck": "quack", 
    "cat": "meow"
}

# Then, we just use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise. get() will return None if the animal is not in the dictionary. Then we just check to see if noise exists. If it does, return noise. Otherwise, return "?" 
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"


# More compact solution which passes in a default value to get()
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')