from audioop import reverse


name=input('Please input file name: ');
count=dict();
try:
    fhand=open(name);
except:
    print('File does not exist.');
    quit();

for wrds in fhand:
    wrds=wrds.rstrip();
    if wrds.startswith('From '):
        #print(wrds);
        wrd=wrds.split();
        word=wrd[1];
        #print(word);
        count[word]=count.get(word,0)+1;
#print(count);

lst=list();
maxword=None;
maxamount=0;
for word,amount in list(count.items()):
    lst.append((amount,word));
    lst.sort(),lst.reverse();
    #print(lst);
    if word is None or amount>maxamount:
        maxword=word;
        maxamount=amount;
        
print(maxamount,maxword);