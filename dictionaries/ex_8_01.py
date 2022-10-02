word=dict();
file=input('Enter file name: ');
try:
    fhand=open(file);
except:
    print('Invalid file name.');
for  lines in fhand:
    lines=lines.rstrip()
    if lines.startswith('From '):
        #print(lines);
        line=lines.split();
        rline=line[2]

        word[rline]=word.get(rline,0)+1;
        print(word);
