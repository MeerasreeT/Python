class library:
    def __init__(self,Library_name,Bookname,Author):
        self.Library_name=Library_name
        self.Bookname=Bookname
        self.Author=Author
        self.book=self.book(self,Library_name,Bookname,Author)
    class book:
        def __init__(self,Library_name):
            self.Library_name=Library_name
    
        def show(self):
            print("Library name:",self.Library_name)
            print("Bookname:",self.Bookname)
            print("Author:",self.Author)
a=library("ABC library","Alchemist","Albert")
a.library.show()
