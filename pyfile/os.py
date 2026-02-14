import os

current_dir =  os.getcwd()
print( 
    f" the cwd is : {current_dir}" 
)



files_here = os.listdir('.')

print(files_here)