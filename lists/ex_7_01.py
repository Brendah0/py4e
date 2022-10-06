count=0
total=0
file=input('Input file name:');

if file=='na na boo boo':
    print('You have been punk\'d');
    quit();


try:
    fhand=open(file);
except:
    print('Error! File missing.');
    quit();

for line in fhand:
    #line=line.upper();
    #print(line);
    if line.startswith('X-DSPAM-Confidence:'):
        number=line.find(':');
        #print(number);
        number=line[number+2:];
        fnumber=float(number);
        #print(fnumber);

        count=count+1;
        total=total+fnumber;
        average=total/count;
        print('The average is',average);
