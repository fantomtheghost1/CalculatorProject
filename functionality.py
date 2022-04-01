import math

cur_operator = ""
value1 = 0
value2 = 0
op_pressed = False

def remove(result):

    global value1, value2

    if not op_pressed:

        if (value1 / 10) < 1:

            value1 = 0

        else:

            value1 = int(str(value1)[:-1])

        result.setText(str(value1))

    elif (op_pressed):

        if (value2 / 10) < 1:

            value2 = 0

        else:

            value2 = int(str(value2)[:-1])

        result.setText(str(value2))


def clear(result):

    global op_pressed, value1, value2, cur_operator

    cur_operator = ""
    value1 = 0
    value2 = 0
    op_pressed = False

    result.setText("0")

def setValue(new_val, result):

    global value1, value2, op_pressed

    if not op_pressed:

        if value1 == 0.0:

            value1 = new_val
            result.setText(str(value1))

        else:

            if len(str(value1)) <= 20:
                value1 = int(str(value1) + str(new_val))

            result.setText(str(value1))

    elif (op_pressed):

        if value2 == 0:

            value2 = new_val
            result.setText(str(value2))

        else:

            if len(str(value2)) <= 20:
                value2 = int(str(value2) + str(new_val))

            result.setText(str(value2))

def setOperator(operator):

    global cur_operator, value1, value2, op_pressed

    if (not op_pressed):

        cur_operator = operator
        op_pressed = True

# button.setStyleSheet change button color when pressed

def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier

def doOperation(result):

    global value1, value2, cur_operator, op_pressed

    if cur_operator != "":

        if cur_operator == "add":

            value1 += value2
            result.setText(str(value1))
            cur_operator = ""

        elif cur_operator == "sub":

            value1 -= value2
            result.setText(str(value1))
            cur_operator = ""

        elif cur_operator == "mult":

            value1 *= value2
            result.setText(str(value1))
            cur_operator = ""

        elif cur_operator == "div":

            if value1 == 0 or value2 == 0:

                result.setText("0")

            else:

                value1 /= value2
                value1 = int(round_half_down(value1))
                result.setText(str(value1))

            cur_operator = ""

        op_pressed = False
        value2 = 0


