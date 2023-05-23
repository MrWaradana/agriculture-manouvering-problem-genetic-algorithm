function c = costarp(sol, tr, r, w)
%turn = sol(1:tr-1);
%turn = 1;
cons=1;
j=1;
c=0;

%condition that rmin>w/2
if r>(w/2) 
    cons = (2*r)/w;
end
% for i=1:trln-1
%     turn(j) = abs(sol(i)-sol(i+1));
%     j=j+1;
% end
for i=1:tr-1
    turn = abs(sol(i)-sol(i+1));
    if turn >= cons
    %U turn
    c = c + ((pi-2)*r + (w*turn));
    else
    %Omega turn
    c = c + (r*((3*pi)-(4*asin(((2*r)+(w*turn))/(4*r)))));
    end
end
%%add for making sure that the inputis on the track 1 an output is 12
if sol(1) ~= 20
    c = c + 50;
end
if sol(tr) ~= 18
    c = c + 50;
end
