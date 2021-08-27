var N,i,temp:integer;
S:real;
begin
  read(N);
  S := 0;
  for i:=1 to N do
  begin
    temp := random(-10,10);
      if((temp mod 3 =0)and(temp mod 5 <>0)) then
        write(temp,' ');
        end;
end.