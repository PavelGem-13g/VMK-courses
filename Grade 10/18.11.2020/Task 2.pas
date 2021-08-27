var M, N:integer;
begin
  read(M,N);
  while (M<=N) do
  begin
    write(M*M*M+' ');
    M:=M+1;
  end;
end.