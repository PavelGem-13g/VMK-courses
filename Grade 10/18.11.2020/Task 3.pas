var i:integer;
begin
  i := 100;
  while (i<1000) do
  begin
    if (i mod 3 = 0) then
      write(i+' ');
    i:=i+1;
  end;
end.