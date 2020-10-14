var apples, chldren:integer;
begin
  write('Введите кол-во яблок ');
  read(apples);
  write('Введите кол-во детей ');
  read(chldren);
  writeln('Осталось каждому - ',apples div chldren);
  writeln('Осталось на компот - ',apples mod chldren);
end.