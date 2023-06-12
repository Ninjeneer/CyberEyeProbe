import subprocess


def parse_lines(lines: list[str]) -> dict:
    osvbs = []

    for line in lines:
        print(line)
        if "OSVDB" in line:
            osvbs.append(line)

    return {
        'osvb': osvbs
    }


def run_nikto_on_target(target: str):
    command = ['./nikto-master/program/nikto.pl', '-h', target]
    nikto_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    lines = nikto_output.stdout.decode().split('\n')

    result = parse_lines(lines)
    print(result)
