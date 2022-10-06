word_list=dict();
romeo=open('romeo.txt');
count=0
#print(romeo);

for words in romeo:
    word=words.split();
    for name in word:
        word_list[name]=word_list.get(name,0)+1;
        #print(word_list);
        count=count+1;
print('Count is: ',count);

maxword=None;
maxvalue=None;
for name,amount in word_list.items():
    if maxword is None or amount>=maxvalue:
        maxword=name;
        maxvalue=amount;
        #print(maxword, maxvalue);
        if maxvalue>=3:
            print(maxword, maxvalue);