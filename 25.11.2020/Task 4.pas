var a,check:integer;
flag:boolean;
begin
  read(a, check);
  flag := false;
  while(a>0) do 
  begin
    if (a mod 10=check) then
      flag := true;
    a := a div 10;
  end;
  if (flag) then
    write('Yes')
  else
    write('No');
end.