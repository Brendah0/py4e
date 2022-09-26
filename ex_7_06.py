num_list=list();
while True:
    num=input('Enter number: ');
    if num=='done':
        break;
    rnum=float(num);
    num_list.append(rnum);
    #print(num);    
   # new_num=num.append(num);
    #print(new_num);
    
maxnum=max(num_list);
minnum=min(num_list);
print('Maximum: ', maxnum);
print('Minimum: ',minnum);