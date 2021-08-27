var a,i:integer;
flag:boolean;
begin
  read(a);
  for i:=2 to a do 
  begin
    if(a mod i = 0) then
      write(i,' ');
  end;
end.