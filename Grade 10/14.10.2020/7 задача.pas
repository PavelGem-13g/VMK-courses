var a:integer;
begin
  write('Введите число ');
  read(a);
  write('Число в обратном порядке ', a mod 10, a mod 100 div 10, a div 100);
end.