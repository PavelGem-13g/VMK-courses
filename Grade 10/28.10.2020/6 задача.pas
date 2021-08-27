var a,b: integer;
begin
  read(a,b);
  if(a mod 2 = 0) and (b mod 2 = 0) then
  begin
    if a>b then
      write(a)
    else 
      write(b)
  end
else
  write('нет четых чисел');
end.