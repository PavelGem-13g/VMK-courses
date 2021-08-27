var sugar, sweets:integer;
     sugarMass, sweetMass:real;
begin
  write('Введите цену конфет ');
  read(sweets);
  write('Введите вес конфет ');
  read(sweetMass);
  
  write('Введите цену сахара ');
  read(sugar);
  write('Введите вес сахара ');
  read(sugarMass);
  
  writeln('Стоимость - ',sweets*sweetMass+sugar*sugarMass);
  writeln('Вес - ', sweetMass+sugarMass);
end.