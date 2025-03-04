#Custom exception
class Error(Exception):
    pass
class ageException(Error):
    pass
class customgeneric(Error):
    pass
year=int(input("Enter year of Birth"))
age=2025-year
try:
    if(age<=30 and age>18):
        pass
    else:
        raise ageException
except:
    print("age is not valid between 18 to 30")
else:
    print("age is valid to play sports")
finally:
    print("age validation complete")
