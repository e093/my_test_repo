class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_sitting = False
        self.is_awake = False
        
    def bark(self):
        print("Woof!")
        
    def sit(self):
        if self.is_sitting:
            print(f"{self.name} is already sitting!")
        else:
            self.is_sitting = True
            print(f"{self.name} sits down.")
            
    def stand(self):
        if self.is_sitting:
            self.is_sitting = False
            print(f"{self.name} stands up")
        else:
            print(f"{self.name} is already standing!.")

    def sleep(self):
        if self.is_awake:
            self.is_awake = False
            print(f"{self.name} sleeps")
        else:
            print(f"{self.name} is already sleeping.")