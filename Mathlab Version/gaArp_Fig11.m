clear;

%data basic Bochtis Conesa:
% tr = 8; %number of track
% w = 2.89;
% r = 3.5;
% trln = 30; %track length

%Harus Set start and end track in costarp.m
%data 2 page 216
% tr = 12; %number of track
% w = 2.5;
% r = 3.5; %di paper angela 2.5  Check Bochtis 2008 paper, page 7, poin 5.2 r=3.5, and w=2.5
% trln = 40; %track length  %b=40m start 1, end 12, c=70m start 2, end 1

%data 20 ini masih error hasilnya maish di atas 300 cek lagi
tr = 20; %number of track start 20, end 18
w = 2.5;
r = 3.5; %di paper angela 2.5  Check Bochtis 2008 paper, page 7, poin 5.2 r=3.5, and w=2.5
trln = 80; %track length  


pSize = (5*tr);
maxGen = 40*tr;%10*tr;
keep = ceil(pSize/10);
elitSol = ones(keep,1);
elit = ones(keep,tr);
runnumber = 10;

rekamGbest = zeros(runnumber, maxGen);
rekamGA = zeros(runnumber,1);
runtimeGA = zeros(runnumber,1);
bestOrder = zeros(runnumber,tr);

tic;
for rec=1:runnumber
%tic;

bestObj = ones(maxGen,1);
cr = ones(pSize,tr);
for i=1:pSize
    cr(i,:)=randperm(tr); % random population of solution/chromosomes
end

cost = zeros(pSize,1);

for s=1:pSize
  c = costarp(cr(s,:),tr, r, w);
  cost(s) =  c; %+ (tr*trln);
end

[tmp, ind] = min(cost);
gbest = tmp;
bestSol = cr(ind,:);
bestCurGen = cr(ind,:);

for g=1:maxGen
%GA operator
        sumCost = sum(cost);
        %calculate the probability of each fitness
        pf = (cost)/sumCost;
        %calculate the cumulative probability of fitness
        cumpf = cumsum(pf);        

        for ip = 1:2:pSize          %initVal:step:endVal — Increment index by the value step on each iteration, or decrements index when step is negative.   
             if rand<=0.7
                child =[];                
                %pick crossover point:
                I = ceil(rand*(tr-2));
                J = ceil(rand*(tr-1));            
                if I==J
                   J = I+1;            
                end
                if I < J
                    cps = I;
                    cpd = J;
                else
                    cps = J;
                    cpd = I;
                end
                indf = find(cumpf-rand>0,1); 
                indm = find(cumpf-rand>0,1);  
                father = cr(indf,:);
                mother = cr(indm,:);

                child(1, cps+1:cpd) = mother(cps+1:cpd);
                child(2, cps+1:cpd) = father(cps+1:cpd);

                restf = [];
                restm = [];
                for i=1:tr
                   if ~ismember(father(i), child(1,:))
                        restf = [restf father(i)];
                    end
                    if ~ismember(mother(i), child(2,:))
                        restm = [restm mother(i)];
                    end
                end
                if size(restf,1) > 0
                    if size(restf,2)==1
                        child(1,cpd) = restf;
                    else
                    child(1, cpd+1:tr) = restf(1:tr-cpd);
                    child(1, 1:cps) = restf(1+tr-cpd:length(restf));      
                    end
                end
                if size(restm,1) > 0
                    if size(restm,2)==1
                        child(2,cpd) = restm;
                    else
                        child(2, cpd+1:tr) = restm(1:tr-cpd);                   
                        child(2, 1:cps) = restm(1+tr-cpd:length(restm));  
                    end
                end
                cr(ip,:) = child(1,:);
                cr(ip+1,:) = child(2,:);
            end
    
            if rand<=0.2 %Mutation           
            
                indp = find(cumpf-rand>0,1);       
                par = cr(indp,:);  
                I = ceil(rand*(tr-2));
                J = ceil(rand*(tr-1));            
                if I==J
                   J = I+1;            
                end

                k = ceil(rand*(3));
                switch k
                    case 1 % Flip
                        cr(indp,I:J) = fliplr(par(I:J));
                    case 2 % Swap
                        cr(indp,[I J]) = par([J I]);
                    case 3 % Slide
                        cr(indp,I:J) = par([I+1:J I]);
                    %otherwise % Do Nothing
                end
            end        
        end    
        cost = zeros(pSize,1);
        for s=1:pSize
            c = costarp(cr(s,:),tr, r, w);
            cost(s) =  c ;%+ (tr*trln);
        end

        [tmp, ind] = min(cost); 
        bestCurGen = cr(ind,:);

        if tmp<gbest
            gbest = tmp;
            bestSol = bestCurGen;
        end

        for i=1:keep/2%ceil(g/2)        
            if g==1
                cr(i,:) = bestSol;
                cost(i) = gbest;              
            else
                [tmp2, ind2] = max(elitSol);
                if tmp < tmp2
                    elit(ind2,:) = bestSol;
                    elitSol(ind2) = tmp; 
                end
            end        
        end
    rekamGbest(rec, g) = gbest;
    runtimeGA(g) = toc;
end
%wtimega = toc;
%fprintf ( 1, '  My GA program took %f seconds to run.\n', wtimega );

rekamGA(rec) = gbest;
bestOrder(rec,:) = bestSol;
gbest;
end
GAtime = toc
[m, ind] = min(rekamGA);
% sol = bestOrder(ind,:)
% mnv = manueverRect(sol, tr, r, w)
h = m + (tr*trln);
fprintf('Total distance = %d \n', h);
fprintf('Headland distance = %d \n', m);

%mean(rekamGA)
%std(rekamGA)
%mean(runtimeGA)
