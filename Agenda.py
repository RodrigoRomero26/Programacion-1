class Contacto():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda():
    def __init__(self):
        self.contacts = []
    
    def addcontact (self, name, phone, email):
        contact = Contacto(name, phone, email)
        self.contacts.append(contact)
        print(f"Contacto {name} agregado.")
    
    def contactlist(self):
        if not self.contacts:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for i, contact in enumerate(self.contacts):
                print(f"{i+1}. Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")
    
    def findcontact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Contacto encontrado - Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")
                return
        print(f"Contacto '{name}' no encontrado en la agenda.")
    
    def editcontact(self, name, newphone, newemail):
        for contacto in self.contacts:
            if contacto.name == name:
                contacto.phone = newphone
                contacto.email = newemail
                print(f"Contacto '{name}' actualizado.")
                return
        print(f"Contacto '{name}' no encontrado en la agenda.")
    
    def close(self):
        print("Agenda cerrada.")