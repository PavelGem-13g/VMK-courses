var n:integer;
begin
  read(n);
  Case n of
    1,2,12: write('Зима');
    3..5: write('Весна');
    6..8: write('Лето');
    9..11: write('Осень');
    else
      writeln('такого месяца не существует');
    end;
end.