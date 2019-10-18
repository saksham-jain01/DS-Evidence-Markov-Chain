d=csvread('distance.csv',1,1);

for i=1:20
    x=bpa([d(i,1) d(i,2) d(i,3) d(i,4) d(i,5)]);
    x
    dlmwrite('BPA_Values.csv',x,'delimiter',',','-append');
end
