function 清空 () {
    我 = 0
    第三人 = 0
    第二人 = 0
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
}
input.onButtonPressed(Button.A, function () {
    if (我 == 0) {
        我 = 1
        basic.showLeds(`
            # # # # #
            . . # . #
            . . # . #
            . # . . #
            # . . # #
            `)
        for (let index = 0; index < 20; index++) {
            radio.sendValue(X, 1)
            basic.pause(100)
        }
    }
    if (我 == 999) {
        X = "a"
        basic.showString(X)
        我 = 0
    }
})
function 比輸贏 () {
    even = 我 * (第二人 * 第三人)
    basic.showNumber(我)
    basic.showNumber(第二人)
    basic.showNumber(第三人)
    if (even == 1 || (even == 8 || (even == 27 || even == 6))) {
        basic.showIcon(IconNames.Asleep)
        basic.pause(100)
    } else if (我 == 1 && (第二人 * 第三人 == 3 || 第二人 * 第三人 == 9)) {
        basic.showIcon(IconNames.Happy)
        basic.pause(100)
    } else if (我 == 2 && (第二人 * 第三人 == 2 || 第二人 * 第三人 == 1)) {
        basic.showIcon(IconNames.Happy)
        basic.pause(100)
    } else if (我 == 3 && (第二人 * 第三人 == 6 || 第二人 * 第三人 == 4)) {
        basic.showIcon(IconNames.Happy)
        basic.pause(100)
    } else {
        basic.showIcon(IconNames.Sad)
    }
}
input.onButtonPressed(Button.AB, function () {
    if (我 == 0) {
        我 = 3
        basic.showLeds(`
            # # # # #
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            `)
        for (let index = 0; index < 20; index++) {
            radio.sendValue(X, 3)
            basic.pause(100)
        }
    }
    if (我 == 999) {
        X = "c"
        basic.showString(X)
        我 = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (我 == 0) {
        我 = 2
        basic.showLeds(`
            # # # # #
            . . # . .
            . # . # #
            # . # . #
            . . # # #
            `)
        for (let index = 0; index < 20; index++) {
            radio.sendValue(X, 2)
            basic.pause(100)
        }
    }
    if (我 == 999) {
        X = "b"
        basic.showString(X)
        我 = 0
    }
})
radio.onReceivedValue(function (name, value) {
    if (X == "a") {
        if (name == "b") {
            第二人 = value
        }
        if (name == "c") {
            第三人 = value
        }
    }
    if (X == "b") {
        if (name == "a") {
            第二人 = value
        }
        if (name == "c") {
            第三人 = value
        }
    }
    if (X == "c") {
        if (name == "a") {
            第二人 = value
        }
        if (name == "b") {
            第三人 = value
        }
    }
    if (我 * (第二人 * 第三人) != 0) {
        basic.pause(5000)
        比輸贏()
        basic.pause(10000)
        清空()
    }
})
let even = 0
let X = ""
let 第二人 = 0
let 第三人 = 0
let 我 = 0
清空()
radio.setTransmitPower(7)
radio.setGroup(69)
我 = 999
