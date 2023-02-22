import subprocess

import utils
import style


def judge_opcount(opcount: int, maximum: int, spicy: int):
    message = str(opcount) + ' / ' + str(maximum) + ' instructions '
    if opcount >= maximum:
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


def judge_validity(operations: str, args: []):
    # Run the checker
    all_args = args.copy()
    all_args.insert(0, "./checker")
    proc = subprocess.run(
        all_args,
        input=operations.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    # Interpret the checker's output
    verdict = utils.get_stdout(proc).strip() == "OK"

    if verdict is True:
        return style.ok("Correct sorting")
    else:
        return style.bad("DOES NOT SORT") + style.unfocused(" Your program's output: ") + operations.replace('\n', ' ')
