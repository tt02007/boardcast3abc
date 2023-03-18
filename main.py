def 清空():
    global 我2, 第三人2, 第二人2
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    我2 = 0
    第三人2 = 0
    第二人2 = 0

def on_button_pressed_a():
    global 我2
    if 我2 == 0:
        我2 = 1
        basic.show_leds("""
            # # # # #
                        . . # . #
                        . . # . #
                        . # . . #
                        # . . # #
        """)
        for index in range(4):
            radio.send_value("a", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def 比輸贏(第二人: number, 我: number, 第三人: number):
    if 我 == 第二人 and 我 == 第三人:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 1 and 第三人 == 2 and 第二人 == 3:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 1 and 第三人 == 3 and 第二人 == 2:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 2 and 第三人 == 1 and 第二人 == 3:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 2 and 第三人 == 3 and 第二人 == 1:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 3 and 第三人 == 1 and 第二人 == 2:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 3 and 第三人 == 2 and 第二人 == 1:
        basic.show_icon(IconNames.ASLEEP)
    elif 我 == 1 and 第三人 == 1 and 第二人 == 3:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 1 and 第三人 == 3 and 第二人 == 3:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 1 and 第三人 == 3 and 第二人 == 1:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 2 and 第三人 == 2 and 第二人 == 1:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 2 and 第三人 == 1 and 第二人 == 1:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 2 and 第三人 == 1 and 第二人 == 2:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 3 and 第三人 == 2 and 第二人 == 2:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 3 and 第三人 == 2 and 第二人 == 3:
        basic.show_icon(IconNames.HAPPY)
    elif 我 == 3 and 第三人 == 3 and 第二人 == 2:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)

def on_button_pressed_ab():
    global 我2
    if 我2 == 0:
        我2 = 1
        basic.show_leds("""
            # # # # #
                        . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
        """)
        for index2 in range(4):
            radio.send_value("a", 3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 我2
    if 我2 == 0:
        我2 = 1
        basic.show_leds("""
            # # # # #
                        . . # . .
                        . # . # #
                        # . # . #
                        . . # # #
        """)
        for index3 in range(4):
            radio.send_value("a", 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global 第二人2, 第三人2
    if name == "b":
        第二人2 = value
    if name == "c":
        第三人2 = value
    basic.pause(1000)
    if 第二人2 * (我2 * 第三人2) != 0:
        比輸贏(第二人2, 我2, 第三人2)
        basic.pause(5000)
        清空()
radio.on_received_value(on_received_value)

第二人2 = 0
第三人2 = 0
我2 = 0
radio.set_transmit_power(7)
radio.set_group(69)
清空()