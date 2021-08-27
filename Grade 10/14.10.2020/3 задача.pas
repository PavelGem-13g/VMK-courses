var salary,K:real;
begin
  write('Введите зарплату ');
  read(salary);
  write('Введите процент налогаоблажения ');
  read(K);
  write('Итоговая зарплата ', salary*((100-K)/100));
end.