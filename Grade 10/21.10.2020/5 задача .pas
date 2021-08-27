var a,b,c:char;
begin
  read(a,b,c);
  if ord(a)>ord(b) then
    begin
    if ord(a)>ord(c) then
      begin
      if ord(b)>ord(c) then
        begin
        write(c,b,a);
        end
      else
        begin
        write(b,c,a);
        end
      end
     else 
       write(b,a,c);
     end
   else
     begin
     if ord(b) > ord(c) then
       begin
       if ord(a)>ord(c) then
         write(c,a,b)
       else
         write(a,c,b);
       end
     else
       write(a,b,c);
     end
end.