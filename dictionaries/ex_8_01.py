word=dict();
emails=dict();
amount=dict();
file=input('Enter file name: ');
try:
    fhand=open(file);
except:
    print('Invalid file name.');
    quit();
for  lines in fhand:
    lines=lines.rstrip()
    if lines.startswith('From '):
        #print(lines);
        line=lines.split();
        date=line[2]
        word[date]=word.get(date,0)+1;

        mail=line[1];
        emails[mail]=emails.get(mail,0)+1;

        mail=mail.split('@');
        mails=mail[1];
        amount[mails]=amount.get(mails,0)+1;
print('**WORD COUNT**');
print(word);
print('**EMAIL COUNT**');
print(emails);
print('**DOMAIN COUNT**');
print(amount);

maxemail=None;
maxcount=None;
for mail,count in emails.items():
    if maxemail is None or count>maxcount:
        maxemail=mail;
        maxcount=count;
print('**MAX MAIL COUNT**')
print(maxemail, maxcount);