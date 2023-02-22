import style


def judge_opcount(opcount: int, max: int, spicy: int):
    message = str(opcount) + ' / ' + str(max) + ' instructions'
    if opcount >= max:
        styled = style.bad(message)
    elif opcount >= spicy:
        styled = style.spicy(message)
    else:
        styled = style.ok(message)
    return styled


def judge_time(time: float):
    message = str(round(time, 2)) + 's'
    if time >= 10:
        styled = style.bad(message)
    elif time >= 0.5:
        styled = style.spicy(message)
    else:
        styled = style.ok(message)
    return styled


def show_test_number(test_number: int):
    return style.unfocused("•TEST " + str(test_number) + ':')


# TODO need to call checker exe
def judge_validity(operations: str, args: []):
    return style.unfocused('Validity unknown')
