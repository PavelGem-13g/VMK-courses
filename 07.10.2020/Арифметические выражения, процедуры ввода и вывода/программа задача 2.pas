program Program1;
var a, hours, minutes: integer;
begin 
write('Ведите число ');
readln(a);
writeln(a div 10000);
writeln(a mod 10000 div 1000);
writeln(a mod 1000 div 100);
writeln(a mod 100 div 10);
writeln(a mod 10);
end.
