%%%% Author: CHANDRAMOHAN T N
%%%% File: Fisher_LDA.m
%%%% c1, c2: denotes class1 and class2 resp.
%%%% w: Direction given by Fisher_LDA

% Finds the direction of Fisher_LDA
function w = LDA(c1, c2)
m1 = mean(c1);
m2 = mean(c2);
for i=1:size(c1, 1)
    c1(i, :) = c1(i, :) - m1;
end
for i=1:size(c2, 1)
    c2(i, :) = c2(i, :) - m2;
end
s1 = c1' * c1;
s2 = c2' * c2;
w = inv(s1 + s2) * (m1 - m2)';
end

% Plots the 2 classes
function Plot_matrix(c1, c2, t)
if size(c1, 2) == 3
    a1 = c1(:, 1);a2 = c1(:, 2);a3 = c1(:, 3);
    b1 = c2(:, 1);b2 = c2(:, 2);b3 = c2(:, 3);
elseif size(c1, 2) == 2
    a1 = c1(:, 1);a2 = c1(:, 2);a3 = zeros(size(c1, 1), 1);
    b1 = c2(:, 1);b2 = c2(:, 2);b3 = zeros(size(c2, 1), 1);
else
    a1 = c1(:, 1);a2 = zeros(size(c1, 1), 1);a3 = zeros(size(c1, 1), 1);
    b1 = c2(:, 1);b2 = zeros(size(c2, 1), 1);b3 = zeros(size(c2, 1), 1);
end
scatter3(a1(:), a2(:), a3(:), '*r');
hold on
title(t);
scatter3(b1(:), b2(:), b3(:), '.b');
hold off
end

% Splits the dataset x into class1 and class2 using labels y.
function [c1, c2] = split(x, y)
c1 = [];c2 = [];
for i=1:size(x, 1)
    if y(i) == 1
        c1 = cat(1, c1, x(i, :));
    else
        c2 = cat(1, c2, x(i, :));
    end
end
end
