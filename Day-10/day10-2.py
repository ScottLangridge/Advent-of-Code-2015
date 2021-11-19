from tqdm import tqdm

def main(raw_input):
    string = raw_input

    for i in range(50):
        print(f'iter:{i + 1} / 50')
        string = look_and_say(string)
        print('\n')

    return len(string)


def look_and_say(string):
    out = ""
    current_char = string[0]
    run_length = 1
    for i in tqdm(string[1:]):
        if i == current_char:
            run_length += 1
        else:
            out = out + str(run_length) + current_char
            current_char = i
            run_length = 1
    out += str(run_length)
    out += current_char
    return out


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
