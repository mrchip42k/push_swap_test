import subprocess
import itertools
import time

import style
import test_print

EXE = "../push_swap/push_swap"


def simulate(cmd: str, args) -> subprocess.CompletedProcess:
    all_args = args.copy()
    all_args.insert(0, cmd)
    return subprocess.run(all_args, stdout=subprocess.PIPE)


def get_stdout(output: subprocess.CompletedProcess) -> str:
    return output.stdout.decode('UTF-8') if output.stdout is not None else ''


def count_lines(text: str) -> int:
    text_arr = text.splitlines()
    count = 0
    for line in text_arr:
        if line is not None and line is not '':
            count = count + 1
    return count


def test(args: [], test_number: int) -> None:
    start_time = time.time()
    proc = simulate(EXE, args)
    time_elapsed = time.time() - start_time
    operations = get_stdout(proc)
    linecount = count_lines(operations)

    print(test_print.show_test_number(test_number)
          + "\t"
          + test_print.judge_opcount(linecount, 12, 7)  # TODO dynamic nums based on arg count
          + '\t\t'
          + test_print.judge_time(time_elapsed)
          + '\t\t'
          + test_print.judge_validity(operations, args)
          + '\t\t'
          + style.unfocused(' '.join(map(str, args)))
          )


def iterate_all_combinations() -> None:
    all_permutations = list(itertools.permutations("12345"))
    print(str(len(all_permutations)) + " combinations found:")
    print(all_permutations)
    print("\n••• ••• ••• BEGIN TESTS ••• ••• •••\n")
    for i in range(len(all_permutations)):
        this_permutation = list(all_permutations[i])
        test(this_permutation, i)
    print("\n••• ••• ••• END TESTS ••• ••• •••\n")


print("Result formatting explanation:")
print(style.ok("This is a parameter that's OK."))
print(style.spicy("This is a parameter that's OK, but not ideal."))
print(style.bad("Not good. Ouch."))
iterate_all_combinations()
