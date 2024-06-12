"""Practice with psychopy"""

from psychopy import core, visual, event

win = visual.Window([800,800], color = "pink")

line_break_to_continue = "/n Press the space bar to continue."
message = visual.TextStim(win, text = "Hello." + line_break_to_continue, color = 'black')
message.draw()
win.flip()
#wanting to print the key pressed
event.waitKeys()
key_press = event.waitKeys()
message_of_key_press = visual.TextStim(win, text = key_press)
message_of_key_press.draw()
win.flip()
core.wait(5)

win.close()
core.close()