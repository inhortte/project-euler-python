#!env python

def reset_name():
    return False, ""

def calculate_name(name):
    return sum([ord(c) - 64 for c in name])

def articulation(filename):
    with open(filename) as f:
        content = f.read()
        name_arr = content.split(",")
        name_arr.sort()
        score = 0
        for idx, name in enumerate(name_arr):
            score += calculate_name(name.replace('"', '')) * (idx + 1)
        return score

def suck_um_in(filename):
    with open(filename) as f:
        reading_name, current_name = reset_name()
        idx = 1
        score = 0

        while True:
            c = f.read(1)
            if not c:
                break
            if c == '"':
                if reading_name:
                    score += calculate_name(current_name) * idx
                    reading_name, current_name = reset_name()
                    idx += 1
                else:
                    reading_name = True
            else:
                if reading_name:
                    current_name += c
                    
        f.close()
        return score
