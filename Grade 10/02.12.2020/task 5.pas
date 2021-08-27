var N,i:integer;
S:real;
begin
  read(N);
  S := 0;
  for i:=1 to N do
  begin
      S := S+random();
  end;
  if (N = 0) then
    write('warning')
  else
    write(S/N);
end.