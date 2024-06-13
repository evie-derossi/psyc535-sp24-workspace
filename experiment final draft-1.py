from psychopy import visual, event, core, gui
import random
import csv

# initialize clock
timer = core.Clock()

# initialize screen
win = visual.Window(size=[1470, 956], monitor='testMonitor', color="white")

# participant info
user_id = gui.Dlg()
user_id.addField("Enter user ID: ")
user_id.show()
if user_id.OK == False: # user cancells -> exits out of experiment
    core.quit()

# saving to data file:
datafile = open(f"experimentdata535_{user_id}.csv", "a")  # uses new data file per new user id
# using append instead of w+ so it adds data instead of overwriting
writer = csv.writer(datafile, delimiter=",")
# writer.writerow([all data you want to append at the end of for loop later])
headers = ["User ID", "Section Number", "Stimulus", "User response", "Feedback", "Response Time"]
writer.writerow(headers)
participant_id = user_id.data[0]

# categories:
man_phrases = ["he", "man", "manly", "male", "him", "boy", "boyish", "masculine",
               "masculinity", "father", "grandfather", "son", "brother", "nephew", "gentleman",
               "bro"]
woman_phrases = ["she", "woman", "women", "girl", "girly", "feminine", "her",
                 "girlish", "ladylike", "mother", "aunt", "grandmother", "sister", "female",
                 "femininity", "daughter"]
feminine_colors = ["light pink", "hot pink", "lavender", "yellow", "light green",
                   "white", "purple"]
masculine_colors = ["red", "green", "blue", "black", "grey", "navy", "orange",
                    "brown"]

phrase_list = woman_phrases + man_phrases # combined lists 
color_list = feminine_colors + masculine_colors
color_categories = ["feminine colors","masculine colors"]
phrase_categories = ["woman","man"]
combo_categories = [["feminine colors/woman","masculine colors/man"],["feminine colors/man","masculine colors/woman"]]
total_list = phrase_list + color_list

###############################
# randomize order of parts
def randomize_1(): # randomizes stimuli list and which part comes first
    stimuli_list = []
    categories = []
    color_num = random.randint(1,3) # chooses either 1 or 2
    if color_num == 1: # color is chosen to be first part
        part1 = "colors"
        part2 = "phrases"
        categories = color_categories
        random.shuffle(color_list)
        stimuli_list = color_list
    else: # phrases are first
        part1 = "phrases"
        part2 = "colors"
        categories = phrase_categories
        random.shuffle(phrase_list)    # randomizes words
        stimuli_list = phrase_list
    return stimuli_list, categories, part1, part2
def randomize_2(): # parts 3 and 4
    categories = combo_categories
    stimuli_list = total_list
    random.shuffle(stimuli_list)
    random.shuffle(categories)
    if categories[0] == ["feminine colors/woman","masculine colors/man"]:
        part3 = "feminine colors/woman vs. masculine colors/man"
        part4 = "feminine colors/man vs. masculine colors/woman"
    else: 
        part4 = "feminine colors/woman vs. masculine colors/man"
        part3 = "feminine colors/man vs. masculine colors/woman"
    return categories, stimuli_list, part3, part4

# stimuli display 
def stim_display(stimuli_list, categories): 
    words_for_section = random.choices(stimuli_list, k=32)
    for stimulus in words_for_section:
        cat_display(categories, part1, part2, part3, part4)
        stim = visual.TextStim(win, text=stimulus, color="black", pos = (0,0))
        stim.draw()
        win.flip()
        start = timer.getTime()
        keypress = event.waitKeys(keyList=["l","r","escape"],timeStamped=timer)
        response, finish = keypress[0]
        time = finish - start
        if response == "escape":
            core.quit()
        return time, response, stimulus
        

def cat_display(categories, part1, part2, part3, part4):
    if part1 == "colors":
        category1 = categories[0] # feminine colors = L
        category2 = categories[1] # masc color = R
    else: #phrases is 1
        category1 = categories[0] # woman L
        category2 = categories[1] # man R
    if part2 == "colors":
        category1 = categories[0] # fem = L
        category2 = categories[1] # masc = R
    else: # part 2 is phrases
        category1 = categories[0] # woman L
        category2 = categories[1] # man R
    if part3 == "feminine colors/woman vs. masculine colors/man":
        category1 = categories[0][0]
        category2 = categories[0][1]
    elif part3 == "feminine colors/man vs. masculine colors/woman":
        category1 = categories[0][0]
        category2 = categories[0][1]
    if part4 == "feminine colors/woman vs. masculine colors/man":
        category1 = categories[0][0]
        category2 = categories[0][1]
    elif part4 == "feminine colors/man vs. masculine colors/woman":
        category1 = categories[0][0]
        category2 = categories[0][1]
    leftcat = visual.TextStim(win, text=category1, pos = (-0.5,0.5), color="black")
    rightcat = visual.TextStim(win, text=category2, pos = (0.5,0.5), color="black")
    leftcat.draw()
    rightcat.draw()

#feedback
def feedback(part1, part2, part3, part4):
    if part1 == "colors":
        category1 = color_categories[0] # fem L 
        category2 = color_categories[1] # masc R
        if response == "l" and stimuli in feminine_colors:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: # sorting fem colors in masc cat
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in masculine_colors:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: #sorting masc col in fem cat
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    else: # phrases is first
        category1 = phrase_categories[0] # fem L 
        category2 = phrase_categories[1] # masc R
        if response == "l" and stimuli in woman_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: # sorting fem words as masc
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in man_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: #sorting masc phr as fem
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    if part2 == "colors":
        category1 = color_categories[0] # fem L 
        category2 = color_categories[1] # masc R
        if response == "l" and stimuli in feminine_colors:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: # sorting fem colors in masc cat
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in masculine_colors:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: #sorting masc col in fem cat
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    else: 
        category1 = phrase_categories[0] # fem L 
        category2 = phrase_categories[1] # masc R
        if response == "l" and stimuli in woman_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: # sorting fem words as masc
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in man_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: #sorting masc phr as fem
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    if part3 == "feminine colors/woman vs. masculine colors/man": # part 3
        category1 = combo_categories[0] # fem L 
        category2 = combo_categories[1] # masc R
        if response == "l" and stimuli in feminine_colors or stimuli in woman_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in masculine_colors or stimuli in man_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    if part4 == "feminine colors/man vs. masculine colors/woman": # part 4
        category1 = combo_categories[0] # fem/man L 
        category2 = combo_categories[1] # masc/woman R
        if response == "l" and stimuli in feminine_colors or stimuli in man_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in masculine_colors or stimuli in woman_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    if part3 == "feminine colors/man vs. masculine colors/woman": 
        category1 = combo_categories[0] # fem/man L 
        category2 = combo_categories[1] # masc/woman R
        if response == "l" and stimuli in feminine_colors or stimuli in man_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in masculine_colors or stimuli in woman_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)
    if part4 == "feminine colors/woman vs. masculine colors/man":
        category1 = combo_categories[0] # fem L 
        category2 = combo_categories[1] # masc R
        if response == "l" and stimuli in feminine_colors or stimuli in woman_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        if response == "r" and stimuli in masculine_colors or stimuli in man_phrases:
            correctfb = "Correct!"
            fb = visual.TextStim(win, text=correctfb,color="green")
        else: 
            wrongfb = "Incorrect!"
            fb = visual.TextStim(win, text=wrongfb,color="red")
        fb.draw()
        win.flip()
        core.wait(0.5)

def run_trial():
        # introduction message
    greet = visual.TextStim(win, text="Welcome to this Implicit Association Test! Thanks for participating. \n"
                                    "Today, we will be measuring the implicit association between gender & color. \n"
                                    "Press any key to continue.", color = "black")
    greet.draw()
    win.flip()
    event.waitKeys()
    intromsg = ("In this IAT experiment, you will respond to a phrase using keys:\n\n"
    "    -[R], indicating a stimulus you associate with the category on the RIGHT side of the screen,\n"
    "    -[L],indicating a stimulus you associate with the category on the LEFT side.\n"
    "Your goal should be to respond to the word/image as quickly and accurately as possible.\n\n"
    "Press any key to continue.")
    intro = visual.TextStim(win, text=intromsg, color="black")
    intro.draw()
    win.flip()
    event.waitKeys()
    stimuli_list, categories, part1, part2, part3, part4 = randomize_1()
    cat_display(categories, part1, part2, part3, part4)
    time, response, stimulus = stim_display(stimuli_list, categories)
    feedback(part1, part2, part3, part4)
    writer.writerow([participant_id, stimulus, response, feedback, time])

# run it
run_trial()
# close everything
datafile.close()
win.close() 
core.quit()