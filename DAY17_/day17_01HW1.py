# Contact class (name, phone, email) + BirthdayContact subclass with days_until_birthday() method. Use datetime.

from datetime import datetime
class Contact:

    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

class Birthdaycontact(Contact):

    def __init__(self,name,phone,email,birth_date):
        super().__init__(name,phone,email)
        self.birth_date = birth_date
    
    def days_until_birthday(self):
        today = datetime.now()

        next_birthday = datetime(today.year,self.birth_date.month,self.birth_date.day)

        if next_birthday < today:
            next_birthday = datetime(today.year+1,self.birth_date.month,self.birth_date.day)

        return (next_birthday - today).days
    
    def __str__(self):
        return (f"{self.name}'s birthday is after {self.days_until_birthday()} days.")
    

name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")
birth_date_str = input("Enter birth date (YYYY-MM-DD): ")

birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

person = Birthdaycontact(name, phone, email, birth_date)

print(person)
