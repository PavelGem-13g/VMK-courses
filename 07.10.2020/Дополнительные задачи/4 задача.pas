var a,b: integer;
begin
  
  read(a);
  read(b);
if (a <> 0) and (b <> 0) then
  if a>b then
    if a mod b = 0 then
      write('Да')
    else 
      write('Нет')
  else  
    if b mod a  = 0 then
      write('Да')
    else 
      write('Нет')
else
  write('Одно из чисел равно 0')
end.