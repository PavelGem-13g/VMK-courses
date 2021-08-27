var n:char;
begin
  read(n);
  Case ord(n) of
    48..57: write('Цифра');
    65..90: write('Заглавная буква');
    97..122: write('Строчная буква');
    else
      writeln('Ни число, ни латинская буква');
    end;
end.