var N,i,temp,temp1,k:integer;
flag:boolean;
S:real;
begin
  read(N);
  S := 0;
  for i:=1 to N do
  begin
    temp := random(-10,10);
      if(temp mod 2 = 0) then
      begin
        flag := true;
        break;
        end
        end;
        if(flag) then
          write('Yes')
        else 
          write('No');
end.