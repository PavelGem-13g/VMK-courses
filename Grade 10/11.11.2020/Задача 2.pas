var k:integer;
begin
  read(k);
  if((k mod 2<>0) and ((k mod 3=0) or (k mod 5=0))) then
    write('Да')
  else
    write('Нет');
end.