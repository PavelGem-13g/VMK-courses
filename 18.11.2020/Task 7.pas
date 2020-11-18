var i,n,k:integer;
begin
  i := 1;
  k := 1;
  read(n);
  while (n>0) do
  begin
    k:=k*(n mod 10);
    n := n div 10;
  end;
  write(k);
end.