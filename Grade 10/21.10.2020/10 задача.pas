var x:integer;
begin
  read(x);
  if (x div 100=3) or ((x mod 100)div 10 = 3) or (x mod 10 = 3) then
  begin
    if (x div 100=3) then
      write('1 число ');
    if ((x mod 100) div 10 = 3) then
      write('2 число ');
    if (x mod 10 = 3) then
      write('3 число ');
  end
  else
    write('Такого числа нет');
end.