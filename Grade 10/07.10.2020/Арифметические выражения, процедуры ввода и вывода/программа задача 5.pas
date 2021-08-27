program Program1;
var S: integer;
    a,P :real;
begin 
write('Ведите число S ');
readln(S);
a := Sqrt(S);
P := a * 4;
write('Сторона = ',a,' периметр ', P);
end.
