file=input('Enter file name: ');
fhand=open(file);

for line in fhand:
    line=line.rstrip();
    if line.startswith('From '):
        words=line.split();
        print(words[2]);
