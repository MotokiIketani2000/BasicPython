text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
result = ""

for word in text.split():
    result += str(sum(1 for char in word if char.isalpha()))
    
print(result)