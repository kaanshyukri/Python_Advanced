class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = [".com", ".bg", ".org", ".net"]

while True:
    line = input()
    if line == "End":
        break
    email = line
    email_check = email.split("@")
    if len(email_check) != 2:
        raise MustContainAtSymbolError('Email must contain @')

    name, domain = email_check
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 character')

    domain = domain.split(".")
    if"." + domain[1] not in domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print("Email is valid")
