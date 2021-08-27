program prog;
var a,max,i:integer;
begin
read(max);
for i:=0 to 1 do
  read(a);
  if a > max then
    max := a;
writeln(max);
end.