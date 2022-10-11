import re


count=0
file=input('Please input file name: ');
try:
    fhand=open(file);
except:
    print('File not found!');
    quit();
regex=input('Please input a regular expression: ');
if len(regex)<0:
    quit();

for line in fhand:
    if re.findall(regex,line):
        count=count+1;
print(count);