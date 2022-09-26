str='X-DSPAM-Confidence: 0.8475 ';

start=str.find(':');
#print(start);

end=str.find('5');
#print(end);

num=str[start+2:end+1];
rnum=float(num);
print(rnum);