var temp,i:integer;
flag:boolean;
begin
  for i:=100 to 1000 do 
  begin
    if(not((i div 100 = 5) or ((i mod 100) or 10 = 5) or (i mod 10 = 5))) then
      write(i,' ');
  end;
end.