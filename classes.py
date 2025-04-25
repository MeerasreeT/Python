class mobilephones:
   
    def __init__(self, brand, number,service):
            self.brand = brand
            self.number=number
            self.service=service
    class simcard:
        def __init__(self,brand,number,service):
            self.brand=brand
            self.number=number
            self.service=service
    def display(self):
            print("Mobile Brand:",self.brand)
            print("Mobile Number:",self.number)
            print("Service      :",self.service)
a=mobilephones("Oppo",8907654321,"Jio")
b=mobilephones("Vivo",7890654678,"Airtel")
a.display()
b.display()
        
