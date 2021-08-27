var n:integer;
flag:boolean;
begin
  flag = false;
  read(n);
  k := n;
  while (n>0) do
  begin
    if(min>(n mod 10)) then
      min := (n mod 10);
    n := n div 10;
  end;
  
  write('min = ',min,' max = ',max);
end.