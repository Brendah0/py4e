count=0
total=0

while True:
  value=input('Please input value: ');
  if value=='done':
    break;

  try:
    rvalue=float(value);
  except:
    print('Bad data!');
    continue;
  count=count+1;
  total=total+rvalue;
  average=total/count;  

print(count);
print(total);
print(average);