var x,y:integer;
begin
  read(x,y);
  if (x>0) and (y>0) then
    write('1 четверть');
  if (x>0) and (y<0) then
    write('4 четверть');
  if (x<0) and (y<0) then
    write('3 четверть');
  if (x<0) and (y>0) then
    write('2 четверть');
  if (x=0) and (y=0) then
    write('Начало координат');
end.