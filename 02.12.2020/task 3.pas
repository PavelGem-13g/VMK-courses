var F0,F1,Fn,N,i:integer;
begin
  F0 := 0;
  F1 := 1;
  read(N);
  for i:=1 to N do
  begin
    Fn := F0+F1;
    if (Fn mod 2 = 0)then
      write(Fn,' ');
    F0 := F1;
    F1 := Fn;
  end;
end.