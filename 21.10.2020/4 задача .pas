var a,b,temp:integer;
begin
  read(a,b);
if a < b then
  temp :=1;
  temp := a;
  a := b;
  b := temp;
write(a,b);
if ((b <> 0) and ((a <> 0)) and (a mod b = 0)) then
  write('Делится')
else
  write('Не делится');
end.