var a,b,c,d: char;
k,flag: integer;
begin
  read(a,b,c,d);
  k:=0;
if(a = '+') or (a = '-') or ((ord(a)>48)and(ord(a)<58)) then
  begin
  k:=k+1;
  if(a = '+') or (a = '-') then
    flag := 1;
  end;
if((ord(b)>48)and(ord(b)<58)) then
  k:=k+1;
if((ord(c)>48)and(ord(c)<58)) then
  k:=k+1;
if((ord(d)>48)and(ord(d)<58)) then
  k:=k+1;
if((k+flag)>3) then
  write('число')
else
  write('не число');
end.