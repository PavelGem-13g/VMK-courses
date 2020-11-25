var n,i, res:integer;
begin
  read(n);
  res := 0;
  for i:=1 to n do 
  begin
    if (i mod 2 = 1) then
      res := res - i
    else
      res := res + i;
  end;
  write(res);
end.