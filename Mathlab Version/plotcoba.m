clc; clear all ;
data = [1,0 ; 1,10 ; 2, 10 ; 2,0 ; 3,0 ; 3,10 ; 4,10 ; 4,0 ; 5,0 ; 5,10];
% figure
hold on
plot(data(:,1),data(:,2),'.r')
% Draw lines
plot(data(1:2,1),data(1:2,2),'b') ;
plot(data(3:4,1),data(3:4,2),'b') ;
plot(data(5:6,1),data(5:6,2),'b') ;
plot(data(7:8,1),data(7:8,2),'b');
plot(data(9:10,1),data(9:10,2),'b') ;
% draw curves 
th = linspace(0,pi) ;
c1 = sum(data(2:3,:))/2 ;
r = 0.5 ;
a1 = [r*cos(th)+c1(1) ; r*sin(th)+c1(2)] ;
plot(a1(1,:),a1(2,:))
c2 = sum(data(4:5,:))/2 ;
a2 = [r*cos(-th)+c2(1) ; r*sin(-th)+c2(2)] ;
plot(a2(1,:),a2(2,:))

%th = linspace(0,pi) 

c3 = sum(data(6:7,:))/2 ;
%c3 = [3.5, 10];
%a3 = [r*cos(pi*sin(th)./th)+c3(1) ; r*sin(pi*sin(th)./th)+c3(2)+1] ;
a3 = [r*cos(2*th)+c3(1) ; r*sin(2*th)+c3(2)+1] ;
plot(a3(1,:),a3(2,:))


%https://www.mathworks.com/matlabcentral/answers/272888-plot-a-heart-using-matlab
