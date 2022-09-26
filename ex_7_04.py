word_list=list();
romeo=open('romeo.txt');
count=0
#print(romeo);

for words in romeo:
    names=words.rstrip();
    nnames=names.split();
    #print(nnames);
    word_list.append(nnames);
print(word_list);
