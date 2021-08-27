var a:char;
begin
  read(a);
  if not(ord(a)>96) and (ord(a) <123) then
    write(chr(ord(a)+32))
  else
    write(a)
end.