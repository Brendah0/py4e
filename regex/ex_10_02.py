import re


tot=0
count=0
file=input('Please input file name: ');
try:
    fhand=open(file);
except:
    print('File not found!');
    quit();

for line in fhand:
    numbers=re.findall('[a-zA-Z]\S*\sR[a-z]\S*: ([0-9]+)',line);
    if len(numbers)>0:
        numbers=list(map(int,numbers));
        #print(numbers);
        for dig in numbers:
            count=count+dig;
            tot=tot+1;
average=count/tot;
print(int(average));