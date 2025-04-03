% mi_script.m
syms x; % Declarar una variable simbólica
f = x^2 + 3*x + 2; % Definir una función simbólica

% Derivar la función
df = diff(f);
disp('Derivada de f(x):');
disp(df);

% Mostrar la derivada en formato LaTeX
disp('Derivada en formato LaTeX:');
disp(latex(df));

% Integrar la función
int_f = int(f);
disp('Integral de f(x):');
disp(int_f);

% Mostrar la integral en formato LaTeX
disp('Integral en formato LaTeX:');
disp(latex(int_f));

% Resolver una ecuación simbólica
sol = solve(f == 0, x);
disp('Soluciones de f(x) = 0:');
disp(sol);

% Mostrar las soluciones en formato LaTeX
disp('Soluciones en formato LaTeX:');
disp(latex(sol));

% Graficar una función
x_vals = 0:0.1:10;
y_vals = sin(x_vals);
plot(x_vals, y_vals);
title('Gráfica de Seno');