import subprocess
import itertools
import time

import style
import test_print
import utils

EXE = "../push_swap/push_swap"


def run_program(cmd: str, args: []) -> subprocess.CompletedProcess:
    all_args = args.copy()
    all_args.insert(0, cmd)
    return subprocess.run(all_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def count_lines(text: str) -> int:
    text_arr = text.splitlines()
    count = 0
    for line in text_arr:
        if line is not None and line is not '':
            count = count + 1
    return count


def test(args: [], test_number: int, argcount: int) -> None:
    start_time = time.time()
    proc = run_program(EXE, args)
    time_elapsed = time.time() - start_time
    operations = utils.get_stdout(proc)
    linecount = count_lines(operations)

    print(test_print.show_test_number(test_number + 1)
          + "\t"
          + test_print.judge_opcount(linecount, argcount)
          + '\t\t'
          + test_print.judge_time(time_elapsed)
          + '\t\t'
          + test_print.judge_validity(operations, args)
          + '\t\t'
          + style.unfocused(' '.join(map(str, args)))
          )


def iterate_all_combinations(permutations_source: str, argcount: int) -> None:
    all_permutations = list(itertools.permutations(permutations_source))
    print(style.unfocused(str(len(all_permutations))
          + " combinations found: "
          + str(all_permutations)
          + "\n")
          )
    for i in range(len(all_permutations)):
        this_permutation = list(all_permutations[i])
        test(this_permutation, i, argcount)


def test_one_argcount(argcount: int) -> None:
    permutations_source: str = ""
    for i in range(1, argcount + 1):
        permutations_source = permutations_source + str(i)

    print("\n\n"
          + style.title("••• ••• ••• Testing all combinations of " + str(argcount) + " arguments. ••• ••• •••")
          + "\n\n"
          )
    iterate_all_combinations(permutations_source, argcount)


# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

print(style.title("Read this tester's README.md for more information."))

print("\n••• ••• ••• BEGIN TESTER ••• ••• •••\n")
for i in range(1, 5 + 1):
    test_one_argcount(i)
print("\n••• ••• ••• END TESTER ••• ••• •••\n")
