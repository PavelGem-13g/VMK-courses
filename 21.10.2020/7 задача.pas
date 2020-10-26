var x:integer;
begin
  read(x);
  if(x>5/3) then
    write(abs(power(cos(x),3))*sqrt(3*x-5)/(power(x,2)*(x-1)))
  else
    write('error');
end.