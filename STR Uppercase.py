class IOString():
    
    def __init__(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input("Enter a String: ")
        
    def print_string(self):
        print("Result is: ", self.str1.upper())
        
        
str1 = IOString()
str2 = IOString()
str3 = IOString()

str1.get_String()
str1.print_string()

str2.get_String()
str2.print_string()

str3.get_String()
str3.print_string()

