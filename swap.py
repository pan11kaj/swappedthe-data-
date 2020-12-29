def write():
    f1 = input('enter your file name:')
    print("//from file one//")
    file1 = open(f1,'r+')
    txt =  file1.read()
    print(txt)
    f2 = input('enter your file name:')
    file2 = open(f2,'r+')
    print("//from file two//")
    txt2 =  file2.read()
    print(txt2)
write()    
def swapped():
    file1 = open('data1.txt','w')
    change = 'this is the text from file2'
    file1.writelines(change)
    file2 = open('data2.txt','w')
    changes = 'this is the text from file1'
    file2.writelines(changes)
    file1 = open('data1.txt','r+')
    file2 = open('data2.txt','r+')
    txt =  file1.read()
    txt2 =  file2.read()
    print("//from file one//")
    print(txt)
    print("//from file two//")
    print(txt2) 

swapped()