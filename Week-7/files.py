f=open('C:\Users\User\Documents\Inspire-Youth-In-STEM\Week-4\text.txt')

print(f.readline())

filename=('C:\Users\User\Documents\Inspire-Youth-In-STEM\Week-4\text.txt')
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    msg ="sorry the file" +filename+"does not exist"


f=open('C:\\Users\\User\\Documents\\Inspire-Youth-In-STEM\\Week-4\\text.txt','r+w')
print(file_name.readlines())