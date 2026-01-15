def open_file(filename): #open_file with exception
    try :
        f = open(filename+".txt","r")
        f = f.read()
        return f
    except FileNotFoundError:
        print("File not found")
        raise SystemExit

def change_str_to_int(file):
    for text in file:
        if '-' in text:
            text = text.replace('-','')
            if text.isdigit():
                text = int("-".join(text))
        if text.isdigit():
            text = int(text)
    return file #stuck in this problem

filename = input()
file = open_file(filename)
file = change_str_to_int(file)
print(file)