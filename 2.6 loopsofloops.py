"""list of items you want partic. to imagine, give an item to imagine a time. For each item, ask 3 questiond"""

stim_list : list[str] = ["dog", "horse", "cow", "pig", "cat"]
q_list : list[str] = ["clear", "detailed", "colorful"]

for animal in stim_list:
    print("Imagine a " + animal + ".")
    for adj in q_list:
        input("How " + adj + " is the image?") 
