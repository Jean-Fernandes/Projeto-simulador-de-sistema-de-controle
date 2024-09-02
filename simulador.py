
# instele o pip antes de usar com o comando: pip install control

#Função tranferência da malha fechada:
import numpy as np
import control as control
import matplotlib.pyplot as plt

num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num , den)
H

"""# Aplicando uma entrada em Degrau"""

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([2.4767])
den = np.array([1, 6.0476, 5.2856, 0.238])
H = control.tf(num, den)

# Calcular resposta ao degrau
t0 = 0
tend = 200
dt = 1e-4
Npontos = int((tend - t0) / dt)
T = np.linspace(t0, tend, Npontos)
t, y = control.step_response(H, T)

# Plotar resposta ao degrau
plt.figure(figsize=(8, 6))  # Definir tamanho da figura

plt.plot(t, y, label='Resposta ao Degrau', color='b', linestyle='-', linewidth=2)  # Plotar a curva

plt.title('Resposta ao Degrau da Função Transferência em malha aberta G(s)')  # Adicionar título
plt.xlabel('Tempo (s)')  # Adicionar rótulo no eixo x
plt.ylabel('Saída')  # Adicionar rótulo no eixo y
plt.grid(True)  # Adicionar grade

plt.legend()  # Adicionar legenda
plt.xlim([t0, tend])  # Limitar o eixo x
plt.ylim([0, 1.30 * max(y)])  # Ajustar o limite do eixo y

plt.show()  # Mostrar o gráfico

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num, den)

# Calcular resposta ao degrau
t0 = 0
tend = 20
dt = 1e-4
Npontos = int((tend - t0) / dt)
T = np.linspace(t0, tend, Npontos)
t, y = control.step_response(H, T)

# Plotar resposta ao degrau
plt.figure(figsize=(8, 6))  # Definir tamanho da figura

plt.plot(t, y, label='Resposta ao Degrau', color='b', linestyle='-', linewidth=2)  # Plotar a curva

plt.title('Resposta ao Degrau da Função Transferência em malha fechada T(s)')  # Adicionar título
plt.xlabel('Tempo (s)')  # Adicionar rótulo no eixo x
plt.ylabel('Saída')  # Adicionar rótulo no eixo y
plt.grid(True)  # Adicionar grade

plt.legend()  # Adicionar legenda
plt.xlim([t0, tend])  # Limitar o eixo x
plt.ylim([0, 1.30 * max(y)])  # Ajustar o limite do eixo y

plt.show()  # Mostrar o gráfico



"""# Polos e Zeros da FT em malha fechada e malha aberta:"""

#MALHA ABERTA

num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num , den)
H
control.pzmap(H)

#MALHA FECHADA

num = np.array([2.4767])
den = np.array([1, 6.0476, 5.2856, 0.238])
H = control.tf(num , den)
H
control.pzmap(H)

"""#Aplicando uma entrada em Rampa"""

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 20
dt = 1e-4
T = np.arange(t0, tend, dt)

# Definir entrada em rampa (rampa unitária)
k = 0.1  # Inclinação da rampa
ramp_input = k * T

# Calcular resposta da função de transferência à entrada em rampa
t, y_ramp = control.forced_response(H, T, ramp_input)

# Plotar resposta à entrada em rampa
plt.figure(figsize=(8, 6))  # Definir tamanho da figura

plt.plot(t, ramp_input, 'r--', label='Entrada em Rampa')  # Plotar entrada em rampa (linha tracejada vermelha)
plt.plot(t, y_ramp, 'b', label='Saída')  # Plotar resposta (linha azul sólida)

plt.title('Resposta à Entrada em Rampa da Função de Transferência em malhda fechada T(s)')  # Adicionar título
plt.xlabel('Tempo (s)')  # Adicionar rótulo no eixo x
plt.ylabel('Amplitude')  # Adicionar rótulo no eixo y
plt.grid(True)  # Adicionar grade

plt.legend()  # Adicionar legenda
plt.xlim([t0, tend])  # Limitar o eixo x

plt.show()  # Mostrar o gráfico

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([2.4767])
den = np.array([1, 6.0476, 5.2856, 0.238])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 200
dt = 1e-4
T = np.arange(t0, tend, dt)

# Definir entrada em rampa (rampa unitária)
k = 1  # Inclinação da rampa
ramp_input = k * T

# Calcular resposta da função de transferência à entrada em rampa
t, y_ramp = control.forced_response(H, T, ramp_input)

# Plotar resposta à entrada em rampa
plt.figure(figsize=(8, 6))  # Definir tamanho da figura

plt.plot(t, ramp_input, 'r--', label='Entrada em Rampa')  # Plotar entrada em rampa (linha tracejada vermelha)
plt.plot(t, y_ramp, 'b', label='Saída')  # Plotar resposta (linha azul sólida)

plt.title('Resposta à Entrada em Rampa da Função da Transferência em malha aberta G(s)')  # Adicionar título
plt.xlabel('Tempo (s)')  # Adicionar rótulo no eixo x
plt.ylabel('Amplitude')  # Adicionar rótulo no eixo y
plt.grid(True)  # Adicionar grade

plt.legend()  # Adicionar legenda
plt.xlim([t0, tend])  # Limitar o eixo x

plt.show()  # Mostrar o gráfico

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 20
dt = 1e-4
T = np.arange(t0, tend, dt)

# Definir entrada em parábola
a = 0.1  # Coeficiente da parábola
parabola_input = a * T**2

# Calcular resposta da função de transferência à entrada em parábola
t, y_parabola = control.forced_response(H, T, parabola_input)

# Plotar resposta à entrada em parábola
plt.figure(figsize=(8, 6))  # Definir tamanho da figura

plt.plot(t, parabola_input, 'r--', label='Entrada em Parábola')  # Plotar entrada em parábola (linha tracejada vermelha)
plt.plot(t, y_parabola, 'b', label='Saída')  # Plotar resposta (linha azul sólida)

plt.title('Resposta à Entrada em Parábola da Função de Transferência em malha fechada T(s)')  # Adicionar título
plt.xlabel('Tempo (s)')  # Adicionar rótulo no eixo x
plt.ylabel('Amplitude')  # Adicionar rótulo no eixo y
plt.grid(True)  # Adicionar grade

plt.legend()  # Adicionar legenda
plt.xlim([t0, tend])  # Limitar o eixo x

plt.show()  # Mostrar o gráfico

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([2.4767])
den = np.array([1, 6.0476, 5.2856, 0.238])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 200
dt = 1e-4
T = np.arange(t0, tend, dt)

# Definir entrada em parábola
a = 0.1  # Coeficiente da parábola
parabola_input = a * T**2

# Calcular resposta da função de transferência à entrada em parábola
t, y_parabola = control.forced_response(H, T, parabola_input)

# Plotar resposta à entrada em parábola
plt.figure(figsize=(8, 6))  # Definir tamanho da figura

plt.plot(t, parabola_input, 'r--', label='Entrada em Parábola')  # Plotar entrada em parábola (linha tracejada vermelha)
plt.plot(t, y_parabola, 'b', label='Saída')  # Plotar resposta (linha azul sólida)

plt.title('Resposta à Entrada em Parábola da Função Transferência em malha aberta G(s)')  # Adicionar título
plt.xlabel('Tempo (s)')  # Adicionar rótulo no eixo x
plt.ylabel('Amplitude')  # Adicionar rótulo no eixo y
plt.grid(True)  # Adicionar grade

plt.legend()  # Adicionar legenda
plt.xlim([t0, tend])  # Limitar o eixo x

plt.show()  # Mostrar o gráfico

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 40
dt = 0.01
T = np.arange(t0, tend, dt)

# Definir entrada degrau (degrau unitário)
step_input = np.ones(len(T))

# Aplicar distúrbio como outro degrau no meio do tempo
disturbance_input = np.zeros(len(T))
disturbance_input[int(len(T)/4):int(len(T)/2)] = 1.0  # Aplicar um degrau como distúrbio

# Calcular resposta da função de transferência ao degrau com distúrbio
t, y_step_with_disturbance = control.forced_response(H, T, step_input + disturbance_input)

# Plotar entrada degrau (com distúrbio) e resposta do sistema
plt.figure(figsize=(10, 6))

plt.plot(t, step_input + disturbance_input, 'r--', label='Distúrbio de degrau unitário')  # Plotar entrada (degrau + distúrbio)
plt.plot(t, y_step_with_disturbance, 'b', label='Resposta ao degrau com distúrbio de degrau')  # Plotar resposta do sistema

plt.title('Resposta ao Degráu com Distúrbio da Função de Transferência')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True)
plt.legend()
plt.xlim([t0, tend])

plt.show()

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 40
dt = 0.01
T = np.arange(t0, tend, dt)

# Definir entrada degrau (degrau unitário)
step_input = np.ones(len(T))

# Aplicar distúrbio como uma rampa ao longo do tempo
disturbance_input = np.linspace(0, 1, len(T))  # Rampa de 0 a 1 ao longo do tempo

# Calcular resposta da função de transferência ao degrau com distúrbio (rampa)
t, y_step_with_ramp_disturbance = control.forced_response(H, T, step_input + disturbance_input)

# Plotar entrada degrau (com distúrbio rampa) e resposta do sistema
plt.figure(figsize=(10, 6))

plt.plot(t, step_input + disturbance_input, 'r--', label='Distúrbio de rampa')  # Plotar entrada (degrau + distúrbio)
plt.plot(t, y_step_with_ramp_disturbance, 'b', label='Resposta ao degrau com distúrbio de rampa')  # Plotar resposta do sistema

plt.title('Resposta ao Degráu com Distúrbio de Rampa da Função de Transferência')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True)
plt.legend()
plt.xlim([t0, tend])

plt.show()

import numpy as np
import control as control
import matplotlib.pyplot as plt

# Definir função de transferência
num = np.array([9.1563, 9.58485, 0.4180])
den = np.array([1, 6.0476, 14.4419, 9.8228, 0.4180])
H = control.tf(num, den)

# Parâmetros da simulação
t0 = 0
tend = 40
dt = 0.01
T = np.arange(t0, tend, dt)

# Definir entrada degrau (degrau unitário)
step_input = np.ones(len(T))

# Aplicar distúrbio como uma parábola ao longo do tempo
disturbance_input = 0.5 * (T - tend/2)**2  # Parábola centrada em t = tend/2 com amplitude 0.5

# Calcular resposta da função de transferência ao degrau com distúrbio (parábola)
t, y_step_with_parabolic_disturbance = control.forced_response(H, T, step_input + disturbance_input)

# Plotar entrada degrau (com distúrbio parábola) e resposta do sistema
plt.figure(figsize=(10, 6))

plt.plot(t, step_input + disturbance_input, 'r--', label='Distúrbio de parábola')  # Plotar entrada (degrau + distúrbio)
plt.plot(t, y_step_with_parabolic_disturbance, 'b', label='Resposta ao degrau com distúrbio de parábola')  # Plotar resposta do sistema

plt.title('Resposta ao Degráu com Distúrbio de Parábola da Função de Transferência')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True)
plt.legend()
plt.xlim([t0, tend])

plt.show()