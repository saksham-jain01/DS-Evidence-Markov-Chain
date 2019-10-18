function [m]= bpa(d)

syms m1 m2 m3 m4 m5;
f=@(m1,m2,m3,m4)(((d(1)*m1)^2+(d(2)*m2)^2+(d(3)*m3)^2+(d(4)*m4)^2+(d(5)*(1-m1-m2-m3-m4))^2)/5)^0.5;
z1=diff(f,m1);
z2=diff(f,m2);
z3=diff(f,m3);
z4=diff(f,m4);

[M1 M2 M3 M4]=solve(z1,z2,z3,z4);
M5=1-M1-M2-M3-M4;
m=[double(M1) double(M2) double(M3) double(M4) double(M5)];
end

