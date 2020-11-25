var n,i:integer;
res:real;
begin
  read(n);
  res := 0;
  for i:=1 to n do 
  begin
    res := res + 1/i;
  end;
  write(res);
end.