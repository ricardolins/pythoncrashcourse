
# letras maisculas e minisculas
name = "ricardo lins"
print(name.title())
print(name.upper())
print(name.lower())

# Concatenando com f
first_name = "ricardo"
last_name = "lins"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)


# Quebra de linha e espaço
print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Removendo o espaço no final da string em execução
favorite_language = "python "
print(favorite_language.rstrip())

#removendo o espaço no final da string definitido

favorite_language = "python "
favorite_language = favorite_language.rstrip()
print(favorite_language)


#removendo o espaço no inicio da string
favorite_language = " python"
print(favorite_language.lstrip())

# Removendo o espaço no começo e no final da string
favorite_language = " python"
print(favorite_language.strip())

