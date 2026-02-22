class Book:
    
    def __init__(self, title,author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"The title is {self.title} and the author is {self.author}"
    
    def __len__(self):
        return len(self.title)
        
        
    
a = Book("Little Mermaid","Jamie")  
print(a)
print(len(a))