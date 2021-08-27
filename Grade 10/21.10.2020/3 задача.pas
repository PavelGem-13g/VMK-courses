var a,b:integer;
begin
  read(a,b);
if ((b <> 0) and (a mod b = 0)) then
  write('Делится')
else
  write('Не делится');
end.