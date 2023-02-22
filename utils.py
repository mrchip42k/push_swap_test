import subprocess


def get_stdout(output: subprocess.CompletedProcess) -> str:
    return output.stdout.decode('UTF-8') if output.stdout is not None else ''
