file=input('Enter file name: ');
fhand=open(file);

for line in fhand:
    line=line.replace('\n\n',' ')
    line=line.rstrip();
    nline=line.splitlines();
    if nline=='':
        break;
    print(nline);
    #lines=' '.join(nline);
    #print(lines);
    #words=lines.split();
    #if words[0]=='From:':
        #print(words);
    