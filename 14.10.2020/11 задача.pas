var a:char;
begin
  write('Введите символ ');
  read(a);
  write(ord(a),' ',ord(ord(a)-1),' ',ord(ord(a)-1));
end.