var a :integer;
begin
  readln(a);
  if((a div 100 > 0) and (a mod 10 = 0)) then
    write('Да')
  else
    write('Нет');
end.