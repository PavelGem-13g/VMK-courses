var k1,k2,b1,b2:integer;
begin
  writeln('Первая прямая ');
  read(k1,b1);
  writeln('Вторая прямая ');
  read(k2,b2);
  
  if (k1=k2) then
    writeln('Прямые не пересекаются')
  else
    begin
    writeln('Прямые пересекаются');
    end;
  
  if (b1>b2) then
    begin
    writeln('Первая прямая выше');
    end
  else
    writeln('Вторая прямая выше');
end.