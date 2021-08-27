var a, b:integer;
begin
  write('Введите четырёхзначное число ');
  read(a);
  write('Новые числа ',a div 1000,a mod 100 div 10, a mod 10 ,'  ', a div 1000, a mod 1000 div 100, a mod 10);
end.