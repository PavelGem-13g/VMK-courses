var V1,V2,t1,t2:real;
begin
  write('Введите V1 ');
  read(V1);
  write('Введите t1 ');
  read(t1);
  write('Введите V2 ');
  read(V2);
  write('Введите t1 ');
  read(t2);
  writeln('Весь путь - ', V1*t1+V2*t2);
  writeln('Средняя скорость', (V1*t1+V2*t2)/(t1+t2));
end.