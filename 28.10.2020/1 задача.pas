var a,b,c,k:integer;
begin
  read(a,b,c);
  k := 0;
  if (a = b) then
    k := k+1;
  if (b = c) then
    k := k+1;
  if (a = c) then
    k := k+1;
  if (k=3) then
    write('3 числа одинаковые');
  if (k=2) then
    write('Странно, что так вышло');
  if (k=1) then
    write('2 числа одинаковые');
end.