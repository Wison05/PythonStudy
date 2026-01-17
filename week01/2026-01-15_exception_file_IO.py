def open_file(filename): #open_file with exception
    try :
        f = open(filename+".txt","r")
        f = f.read()
        lines = f.strip().split("\n")
        return [line for line in lines if line.strip()]
    except FileNotFoundError:
        print("File not found")
        raise SystemExit

def try_parse_int(line: str):
    t = line.strip()
    try:
        return True, int(t)
    except ValueError:
        return False, 0

def change_type_cal(lines):
    invalid_lines = []
    total = 0
    for line in lines:
        ok, value = try_parse_int(line)
        if ok:
            total += value
        else:
            invalid_lines.append(line)
    return invalid_lines, total

filename = input()
file = open_file(filename)
file,total = change_type_cal(file)
for i in file:
    print("Invalid line:",i)
print("sum:",total)
