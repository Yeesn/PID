import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 定义输入变量
error = ctrl.Antecedent(np.arange(-10, 11, 1), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 11, 1), 'error_dot')

# 定义输出变量
output = ctrl.Consequent(np.arange(-10, 11, 1), 'output')

# 定义模糊集合
error['NB'] = fuzz.trimf(error.universe, [-10, -10, -5])
error['NM'] = fuzz.trimf(error.universe, [-10, -5, ])
error['NS'] = fuzz.trimf(error.universe, [-5, , 5])
error['ZO'] = fuzz.trimf(error.universe, [, 5, 10])
error['PS'] = fuzz.trimf(error.universe, [5, 10, 10])
error['PM'] = fuzz.trimf(error.universe, [, 5, 10])
error['PB'] = fuzz.trimf(error.universe, [5, 10, 10])

error_dot['NB'] = fuzz.trimf(error_dot.universe, [-10, -10, -5])
error_dot['NM'] = fuzz.trimf(error_dot.universe, [-10, -5, ])
error_dot['NS'] = fuzz.trimf(error_dot.universe, [-5, , 5])
error_dot['ZO'] = fuzz.trimf(error_dot.universe, [, 5, 10])
error_dot['PS'] = fuzz.trimf(error_dot.universe, [5, 10, 10])
error_dot['PM'] = fuzz.trimf(error_dot.universe, [, 5, 10])
error_dot['PB'] = fuzz.trimf(error_dot.universe, [5, 10, 10])

output['NB'] = fuzz.trimf(output.universe, [-10, -10, -5])
output['NM'] = fuzz.trimf(output.universe, [-10, -5, ])
output['NS'] = fuzz.trimf(output.universe, [-5, , 5])
output['ZO'] = fuzz.trimf(output.universe, [, 5, 10])
output['PS'] = fuzz.trimf(output.universe, [5, 10, 10])
output['PM'] = fuzz.trimf(output.universe, [, 5, 10])
output['PB'] = fuzz.trimf(output.universe, [5, 10, 10])

# 定义规则
rule1 = ctrl.Rule(error['NB'] & error_dot['NB'], output['NB'])
rule2 = ctrl.Rule(error['NB'] & error_dot['NM'], output['NM'])
rule3 = ctrl.Rule(error['NB'] & error_dot['NS'], output['NS'])
rule4 = ctrl.Rule(error['NB'] & error_dot['ZO'], output['ZO'])
rule5 = ctrl.Rule(error['NB'] & error_dot['PS'], output['PS'])
rule6 = ctrl.Rule(error['NB'] & error_dot['PM'], output['PM'])
rule7 = ctrl.Rule(error['NB'] & error_dot['PB'], output['PB'])

rule8 = ctrl.Rule(error['NM'] & error_dot['NB'], output['NM'])
rule9 = ctrl.Rule(error['NM'] & error_dot['NM'], output['NS'])
rule10 = ctrl.Rule(error['NM'] & error_dot['NS'], output['ZO'])
rule11 = ctrl.Rule(error['NM'] & error_dot['ZO'], output['PS'])
rule12 = ctrl.Rule(error['NM'] & error_dot['PS'], output['PM'])
rule13 = ctrl.Rule(error['NM'] & error_dot['PM'], output['PB'])
rule14 = ctrl.Rule(error['NM'] & error_dot['PB'], output['PB'])

rule15 = ctrl.Rule(error['NS'] & error_dot['NB'], output['NS'])
rule16 = ctrl.Rule(error['NS'] & error_dot['NM'], output['ZO'])
rule17 = ctrl.Rule(error['NS'] & error_dot['NS'], output['PS'])
rule18 = ctrl.Rule(error['NS'] & error_dot['ZO'], output['PM'])
rule19 = ctrl.Rule(error['NS'] & error_dot['PS'], output['PB'])
rule20 = ctrl.Rule(error['NS'] & error_dot['PM'], output['PB'])
rule21 = ctrl.Rule(error['NS'] & error_dot['PB'], output['PB'])

rule22 = ctrl.Rule(error['ZO'] & error_dot['NB'], output['ZO'])
rule23 = ctrl.Rule(error['ZO'] & error_dot['NM'], output['PS'])
rule24 = ctrl.Rule(error['ZO'] & error_dot['NS'], output['PM'])
rule25 = ctrl.Rule(error['ZO'] & error_dot['ZO'], output['PB'])
rule26 = ctrl.Rule(error['ZO'] & error_dot['PS'], output['PB'])
rule27 = ctrl.Rule(error['ZO'] & error_dot['PM'], output['PB'])
rule28 = ctrl.Rule(error['ZO'] & error_dot['PB'], output['PB'])

rule29 = ctrl.Rule(error['PS'] & error_dot['NB'], output['PS'])
rule30 = ctrl.Rule(error['PS'] & error_dot['NM'], output['PM'])
rule31 = ctrl.Rule(error['PS'] & error_dot['NS'], output['PB'])
rule32 = ctrl.Rule(error['PS'] & error_dot['ZO'], output['PB'])
rule33 = ctrl.Rule(error['PS'] & error_dot['PS'], output['PB'])
rule34 = ctrl.Rule(error['PS'] & error_dot['PM'], output['PB'])
rule35 = ctrl.Rule(error['PS'] & error_dot['PB'], output['PB'])

rule36 = ctrl.Rule(error['PM'] & error_dot['NB'], output['PM'])
rule37 = ctrl.Rule(error['PM'] & error_dot['NM'], output['PB'])
rule38 = ctrl.Rule(error['PM'] & error_dot['NS'], output['PB'])
rule39 = ctrl.Rule(error['PM'] & error_dot['ZO'], output['PB'])
rule40 = ctrl.Rule(error['PM'] & error_dot['PS'], output['PB'])
rule41 = ctrl.Rule(error['PM'] & error_dot['PM'], output['PB'])
rule42 = ctrl.Rule(error['PM'] & error_dot['PB'], output['PB'])

rule43 = ctrl.Rule(error['PB'] & error_dot['NB'], output['PB'])
rule44 = ctrl.Rule(error['PB'] & error_dot['NM'], output['PB'])
rule45 = ctrl.Rule(error['PB'] & error_dot['NS'], output['PB'])
rule46 = ctrl.Rule(error['PB'] & error_dot['ZO'], output['PB'])
rule47 = ctrl.Rule(error['PB'] & error_dot['PS'], output['PB'])
rule48 = ctrl.Rule(error['PB'] & error_dot['PM'], output['PB'])
rule49 = ctrl.Rule(error['PB'] & error_dot['PB'], output['PB'])

# 定义控制系统
pid_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7,
     rule8, rule9, rule10, rule11, rule12, rule13, rule14,
     rule15, rule16, rule17, rule18, rule19, rule20, rule21,
     rule22, rule23, rule24, rule25, rule26, rule27, rule28,
     rule29, rule30, rule31, rule32, rule33, rule34, rule35,
     rule36, rule37, rule38, rule39, rule40, rule41, rule42,
     rule43, rule44, rule45, rule46, rule47, rule48, rule49])

pid = ctrl.ControlSystemSimulation(pid_ctrl)

# 模拟控制
pid.input['error'] = 5
pid.input['error_dot'] = 2
pid.compute()
print(pid.output['output'])