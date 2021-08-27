var N,i,chet,nechet:integer;
S:real;
begin
  read(N);
  S := 0;
  for i:=1 to N do
  begin
      if(random(-10,10) mod 2 =0) then
        chet := chet +1
      else
      begin
        nechet := nechet+1;
        end;
        
  end;
  if (chet>nechet) then
    write('Четных больше')
  else
    write('Нечетных больше');
end.