var a, b:integer;
begin
  write('Введите двузначное число ');
  read(a);
  write('Введите цифру ');
  read(b);
  write('Новое число ',b,a div 10,b,a mod 10,b);
end.