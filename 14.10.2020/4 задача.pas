var floors,flats, myFlat:integer;
begin
  write('Введите кол-во этажей ');
  read(floors);
  write('Введите кол-во квартир на этаже ');
  read(flats);
  write('Введите нужную квартиру ');
  read(myFlat);
  writeln('Подъезд - ', (myFlat div (floors*flats))+1);
  writeln('Этаж - ', (myFlat div floors)+1);
end.