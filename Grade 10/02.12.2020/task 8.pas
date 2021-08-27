var N,i,temp,temp1,k:integer;
S:real;
begin
  read(N);
  S := 0;
  temp1 := random(-10,10);
  for i:=2 to N do
  begin
    temp := random(-10,10);
      if(abs(temp1-temp)=1) then
        k:=k+1;
        end;
        write(k);
end.