name = ''
def get_string(m):
    try:
        string = str(input(m))
        return string
    except:
        print('Input has error try again\n')
        get_string(m)
def get_int(m):
    try:
        integer = int(input(m))
        return integer
    except:
        print('Input has error try again\n')
        get_int(m)
def pause():
    input('press Enter to continue')
def get_name():
    global name
    name = get_string('Your Name - ')
def display(name):
    print('Your Name is - ',name)
    pause()
    return 1
def ndisplay(name):
    n = get_int('Character count: ')
    print(n,'Charcters from your name:\n', name[0:n])
    pause()
    return 1
def countv(name):
    count = 0
    index = 0
    length = len(name)
    while index < length:
        l = name[index]
        if l.lower() in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
        elif l.upper() in ('A', 'E', 'I', 'O', 'U'):
            count = count + 1
        index = index + 1
    
    print('Vowel count- ', count)
    pause()
    return 1

def reverse(name):
    reversed_string = ''
    length = len(name) -1
    
    while length >= 0:
        reversed_string = reversed_string +  name[length]
        
        length = length - 1
    print('Reversed name - ', reversed_string)
    pause()
    return 1
def options():
   
    print(
        '----------------------------\n\n',
        '-------------------------------\n',
        'Select an Option\n',
        '-------------------------------\n',
        '1      Display Name\n',
        '2      Display characters from left\n',
        '3      Count the vowels\n',
        '4      Reverse\n',
        '0      Exit\n',
        '-------------------------------',
        )
    op = get_int('Select:    ')
    global name
    if(op == 1):
        if(display(name)): 
            return options()
    if(op == 2):
        if(ndisplay(name)):
            return options()
    if(op==3):
        if(countv(name)):
            return options()
    if(op==4):
        if(reverse(name)):
            return options()
    if(op == 0):
        return 1 
    
    print(op,'Try Again\n')
    return options()
    

get_name()
options()
