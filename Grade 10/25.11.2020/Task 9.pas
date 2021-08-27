var n,i:integer;
res:real;
begin
  read(n);
  res := 0;
  while (i<=n) do
  begin
    res := res + i/(i+1);
    i := i+1;
  end;
  write(res);
end.