var n:integer;
begin
  read(n);
  Case n-1 of
    1: write('Январь');
    2: write('Февраль');
    3: write('Март');
    4: write('Апрель');
    5: write('Май');
    6: write('Июнь');
    7: write('Июль');
    8: write('Август');
    9: write('Сентярь');
    10: write('Октябрь');
    11: write('Ноябрь');
    12: write('Декабрь')
    else
      writeln('такого месяца не существует');
    end;
  Case n+1 of
    1: write('Январь');
    2: write('Февраль');
    3: write('Март');
    4: write('Апрель');
    5: write('Май');
    6: write('Июнь');
    7: write('Июль');
    8: write('Август');
    9: write('Сентярь');
    10: write('Октябрь');
    11: write('Ноябрь');
    12: write('Декабрь')
    else
      writeln('такого месяца не существует');
  end;
end.