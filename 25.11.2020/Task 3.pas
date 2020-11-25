var a,min, max,temp:integer;
begin
  min := 10;
  max := -1;
  read(a);
  while(a>0) do 
  begin
    temp := a mod 10;
    if (temp<min) then
      min := temp;
    if (temp>max) then
      max := temp;
    a := a div 10;
  end;
  write('min = ',min,' max = ',max);
end.