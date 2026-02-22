class MathUtils:
    
    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operations")
        
        
# e=MathUtils
# print(e.add(3,57),"\n",)
# e.description()

#without object

MathUtils.description()
print(MathUtils.add(4,6))