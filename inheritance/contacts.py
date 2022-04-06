class ContactList(list):
    def search(self, name: str) -> list:
        """Return all contacts that contain the search value in their name.

        Args:
            name (list): with all contacts that match the search name.
        """
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()
    """
    Note that this is a class variable, if I had set this in the __init__ method as 
    self.all_contacts, it would be an instance variable and altering it wouldn't 
    change the value of this list.
    """

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(
            f"""If it was a real system it would send {order} order to {self.name}."""
        )


class AdressHolder:
    def __init__(self, street, city, state, code) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AdressHolder):
    def __init__(self, name, email, phone, street, city, state, code) -> None:
        Contact.__init__(name, email)
        AdressHolder.__init__(self, street, city, state, code)
        self.phone = phone


class MailSender:
    def send_email(self, message):
        print(f"Sending email to {self.email}")


class EmailableContact(Contact, MailSender):
    pass


if __name__ == "__main__":
    emailable_contact = EmailableContact("Luciana", "luciana@email.com")
    emailable_contact.send_email("test message")
