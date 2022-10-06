from token import NEWLINE


name=input('Please input file name: ');
count=dict();
lst=list();
try:
    fhand=open(name);
except:
    print('File does not exist.');
    quit();


for wrds in fhand:
    wrds=wrds.rstrip();
    if wrds.startswith('From '):
        wrds=wrds.split();
        wrd=wrds[5].split(':');
        #print(wrd);
        tym=wrd[0];
        #print(tym);
        count[tym]=count.get(tym,0)+1;
#print(count);

for tym,amount in list(count.items()):
    lst.append((tym,amount));
    lst.sort()
print(*lst, sep='\n');