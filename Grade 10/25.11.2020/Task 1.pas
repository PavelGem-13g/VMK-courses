var a,s:integer;
begin
  s := 1;
  read(a);
  while(a>0) do 
  begin
    s := s*(a mod 10);
    a := a div 10;
  end;
  write(s);
end.