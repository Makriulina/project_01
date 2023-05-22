

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
   return s.replace('!', '')
print(remove_exclamation_marks("!"))
print(remove_exclamation_marks("Oh, no!!!"))
print(remove_exclamation_marks("Hi! Hello!"))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
  if len(s)>0 and s[-1] == '!':
            return s[:-1]
  return s
print(remove_last_em("Hi!"))
print(remove_last_em ("Hi!!!"))
print(remove_last_em("!Hi"))


