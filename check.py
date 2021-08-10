import os 
import shutil

def up_one_level(times):
    time=0
    while times >=time :
        time+=1
        print(time)
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        print(os.getcwd())
up_one_level(1)
os.chdir('D:')
print(os.getcwd())
os.chdir('books organised')
print(os.getcwd())
print(os.listdir())
files=os.listdir()
os.chdir('C:')
print(os.getcwd())
os.chdir('programming\check_files_update')    
print(os.listdir())     
os.chdir('books')
for item in os.listdir():
    for file in files:
        if item == file:
            print(item)
            print(file)
            os.chdir(item) #now in the specific folder
            copies = os.listdir()
            os.chdir("D:")
            os.chdir(item)
            originals=os.listdir()
            print(os.listdir())
            print("number of books in " + item +" = "+str(len(os.listdir())))
            for book in originals:
                for copy in copies:
                              if book == copy:
                                  print("success!")
                                  print(book)
                                  print(copy)
                              else:
                                  os.chdir("C:")
                                  print(os.listdir())
                                  dest = (f'D:\\books organised\{item}\{copy}')
                                  print(dest)
                                  shutil.copy( copy, dest )

            

            