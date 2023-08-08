#error and exeception handling

class UnderAgeError(Exception):
  def __init__(self, message):
    super().__init__(message)
    
class ZeroAgeError(Exception):
  def __init__(self, message):
    super().__init__(message)




def hotel():
    try:
        name=input('enter your name: ')
        age=int(input('enter your age: '))
        if(age<=0):
            raise ZeroAgeError('Age can not be zero or less')
        
        elif(age<18):
            raise UnderAgeError('You are under age')
        else:
            print(f'{name} youre welcome')
    except UnderAgeError as e:
        print(e)
    except ZeroAgeError as e:
        print(e)
    except TypeError:
        print('Error')
    else:
        print(f'{name} you are welcome to our hotel')
    finally:
        print('thanks for comming')
        
hotel()
print('............................................................................')
 
#file handling  
"""
opening files
   file_object = open(file_path, mode)
modes are a,r,w,a+,r+,w+ and each has its wn specific functionality 
files are opened in text or binary mode by adding t or b to the mode

closing files
after working with a files is essential to close it to avoid errors
    file_object.close()
    
we can use the "with open" to avoid closing the file as the file closes automatically after use or when it runs into an exception
    
reading from and writing to a file
    read() -reads entire file content
    readline() -Reads a single line from the file.
    readlines() -Reads all the lines of the file and returns them as a list.

    write()
"""

try:
    # Writing to a file
    with open("text.txt", "w") as file_object:
        file_object.write("python \n")
        file_object.write("java \n")
        file_object.write("dart \n")
        file_object.write("javascript \n")

    # Reading from the file
    with open("text.txt", "r") as file_content:
        content = file_content.read()
        print("Original Content:")
        print(content)

    # Appending a new line
    with open("text.txt", "a") as file_object:
        file_object.write("I hate php though\n")

    # Reading the updated content
    with open("text.txt", "r") as file_object:
        updated_content = file_object.read()
        print("Updated Content:")
        print(updated_content)

except FileNotFoundError:
    print("File not found error occurred.")
except IOError:
    print("An error occurred while performing I/O operation on the file.")
except Exception as e:
    print("An error occurred:", str(e))
