var a, b:integer;
begin
  write('Введите число ');
  read(a);
  write('Введите вставляемое число ');
  read(b);
  write('Число в обратном порядке ',a div 100, b,a mod 10);
end.