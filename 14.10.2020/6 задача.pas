var day:integer;
begin
  write('Введите день ');
  read(day);
  if day mod 7 = 0 then
    write('День недели - 7')
  else
    write('День недели - ', day mod 7)
end.