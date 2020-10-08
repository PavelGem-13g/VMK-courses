program Program1;
var a, b, S, P: integer;
begin 
write('Ведите число a ');
readln(a);
write('Ведите число b ');
readln(b);
S := a*b;
P := a * 2 + b * 2;
write('Площадь = ',S,' периметр ', P);
end.
