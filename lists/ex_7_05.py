file=input('Please input file name:');
count=0;
try:
  fhand=open(file);
except:
    print('File not found!');
    quit();

for line in fhand:    
    line=line.rstrip();
    #print(line);
    if line.startswith('From '):
        #print(line);
        nline=line.split();
        email=nline[1:2];
        count=count+1
        print(email);
print('There were '+ str(count) +' lines in the file with From as the first word.');