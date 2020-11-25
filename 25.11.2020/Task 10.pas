var n,i:integer;
res:real;
begin
  read(n);
  res := 0;
  i :=1;
  while (i<=n) do
  begin
    if(i mod 2 = 1) then
      res := res + (i)/(i+2);
    else
      res := res - (i)(i+2);
    i := i+1;
  end;
  write(res);
end.