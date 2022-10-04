def on_button_pressed_a():
    global counter
    counter += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counter
    counter += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

counter = 0