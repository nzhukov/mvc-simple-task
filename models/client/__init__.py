
class Client():
    def __init__(self, first_name, last_name, email, city, index, address):
        self.__client = {"first_name": first_name, "last_name":last_name, "email": email}


    def __str__(self):
        return f'{str(self.__client.get("first_name"))}'


    @property
    def full_name(self):
        return f"{self.__client.get('first_name')} {self.__client.get('last_name')}" 
    
