program Program1;
var a, hours, minutes: integer;
begin 
write('Ведите кол-во минут ');
readln(a);
hours := a div 60;
minutes := a - hours*60;
write('Часы = ',hours,', минуты = ', minutes);
end.
