class Employee:
    #Initiating the constructor
    def __init__(self):
        print("Started executing attributes")
        self.id = 123
        
        self.salary = 50000
        self.designation = "SDE"
        print("attributes are executed")

    def travel(self, destination):
        print("This travel function was called manually")
        print("Traveling to", destination)

#Creating an object of the class employee

sam = Employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
print(sam.travel("Delhi"))

        