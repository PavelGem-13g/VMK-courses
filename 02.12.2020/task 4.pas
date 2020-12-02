var F0,F1,Fn,N,i,k,S:integer;
begin
  F0 := 0;
  F1 := 1;
  read(N,k);
  for i:=1 to N do
  begin
    Fn := F0+F1;
    if (Fn < k)then
      S := S +k;
    F0 := F1;
    F1 := Fn;
  end;
  write(S);
end.