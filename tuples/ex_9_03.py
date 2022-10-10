from curses.ascii import isalpha
import string;


lines=list();
count=dict()
freq=list()

fyl=input('Input file name: ');
try:
    fhand=open(fyl);
except:
    print('Error!');
    quit();
#print(fhand);

alphabet=list(string.ascii_lowercase);
#print(alphabet);

for line in fhand:
    line=line.translate(str.maketrans('','',string.punctuation));
    line=line.lower();
    words=line.split();
    #print(words);
    for word in words:
        #print(word);
        for letter in word:
            if (letter in alphabet):
                #print(letter);
                count[letter]=count.get(letter,0)+1;

print(count)

for k,v in list(count.items()):
    freq.append((v,k));
    freq.sort();
    freq.reverse();
print(freq);    