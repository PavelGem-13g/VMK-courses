var i:integer;
k:char;
begin
  i := 0;
  repeat
    read(k);
    i:=i+1;
    until ((k='*'));
  write(i);
end.