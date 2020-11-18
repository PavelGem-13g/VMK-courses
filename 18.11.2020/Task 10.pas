var n,k:integer;
flag:boolean;
begin
  flag := false;
  read(n,k);
  while ((n>0) and (not(flag))) do
  begin
    if(k = (n mod 10)) then
      flag := true;
    n := n div 10;
  end;
  if(flag) then
    write('Yes')
  else
    write('No');
  
end.