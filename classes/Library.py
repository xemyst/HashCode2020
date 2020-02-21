class Library:
    def __init__(self,id,time,maxScan,bookDict):
        self.id = int(id)
        self.time=int(time)
        self.books=[]
        self.maxScan=int(maxScan)
        self.bookDict = bookDict
        self.read = []

    def processBooks(self,bookString):
        books = bookString.split(' ')
        books[-1] = books[-1].split('\n')[0]
        self.books = books

    def maxBooks(self, leftDays):
        read = self.read
        temp = {}
        for book in self.books:
            book = int(book)
            temp[book] = self.bookDict[book]

        self.books = sorted(temp, key=temp.get)
        leftBooks = self.books
        for x in range(leftDays):
            if self.maxScan >= len(leftBooks):
                leftBooks = map(lambda x: str(x),leftBooks)
                read += [*leftBooks]
                break
            else:
                for book in range(self.maxScan):
                    read += [str(leftBooks.pop())]

    def __str__(self):
        print('Library:', self.id,
              '\nmaxScan:', self.maxScan,
              '\nquant readedBooks', len(self.read) )
        return ''
