var i,n,k:integer;
begin
  i := 1;
  k := 1;
  read(n);
  while (i<=n) do
  begin
    k:=k*i;
    i:=i+1;
  end;
  write(k);
end.