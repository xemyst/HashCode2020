from classes.Library import Library
Books = {}
Librarys = []
maxDays = 0
files = [
# 'a_example.txt',
# 'c_incunabula.txt',
# 'b_read_on.txt',
# 'd_tough_choices.txt',
# 'e_so_many_books.txt',
# 'f_libraries_of_the_world.txt'
]
def readFirstLine(input):
    file = ''
    file = open(files[input],'r')
    firstLine = file.readline().split(' ')
    firstLine[-1] = firstLine[-1].split('\n')[0]
    return firstLine, file

def readBooks(file,nBooks):
    values = file.readline().split(' ')
    values[-1] = values[-1].split('\n')[0]
    for x in range(int(nBooks)):
        Books[x] = values[x]

def configLibrarys(file,nLibrarys):
    global Librarys, Books
    for x in range(int(nLibrarys)):
        data = file.readline().split(' ')
        data[-1] = data[-1].split('\n')[0]
        Librarys += [Library(x,data[1],data[2], Books)]
        Librarys[x].processBooks(file.readline())

def read(x):
    return readFirstLine(x)

def signup():
    global Librarys
    # key: library, value: init
    order = {}
    currentDay = 0
    for library in Librarys:
        if maxDays >= (currentDay + library.time):
            order[library.id] = currentDay
            currentDay += library.time
        else:
            continue
    return order

def scanBooks(order):
    for key in order.keys():
        leftDays = maxDays - (order[key] + Librarys[key].time)
        Librarys[key].maxBooks(leftDays)

def output(order,x):
    lines= [len(order)]

    for key in order.keys():
        if len(Librarys[key].read) > 0 :
            lines += [str(key) + ' ' + str(len(Librarys[key].read))]
            lines += [' '.join(Librarys[key].read)]
        else:
            lines[0] = lines[0] - 1
    lines[0] = str(lines[0])
    out = files[x].split('.txt')[0] + '.out'
    f = open(out,'a')
    f.write('\n'.join(lines))
    f.close()

def problemSolver(x):
    global maxDays
    fl, file = read(x)
    maxDays = int(fl[2])
    readBooks(file,fl[0])
    configLibrarys(file,fl[1])
    order = signup()
    scanBooks(order)
    file.close()
    output(order,x)

def main():
    global Books, Library, maxDays
    Books = {}
    Librarys = []
    maxDays = 0
    for x in range(len(files)):
        problemSolver(x)

if __name__ == '__main__':
    main()
