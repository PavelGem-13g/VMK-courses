var N,a,d,i:integer;
begin
  read(N,a,d);
  for i:=1 to N do
  begin
    write(a+(i-1)*d,' ');
  end;
end.