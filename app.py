import apps.python_modules as py_module

result=py_module.add(2,3)

print('Hello', 'how are you?')
print(f'addition of 3 and 2 is {result}')

result=py_module.subtract(3,2)

print(f'subtraction of 3 and 2 is {result}')

from apps.python_modules import generate_random_number as gnr


for i in range(0, 10): 
    random_number=gnr(10000000,999999999)
    print(f'index number {i}, generated number: {random_number}')
    

from apps.python_modules import multiply as multiply

nodes=int(input('Enter node count: '))
ps_per_node=int(input('Enter process per node: '))

total_capacity=multiply(nodes, ps_per_node) 

print(f'Total Capacity {total_capacity}')

total_tasks=403

from apps.python_modules import division as divide, remainder as rem

tasks_per_node=divide(total_tasks,nodes)
leftover_tasks=rem(total_tasks,nodes)

print(f"Infrastructure Report".center(40, '-'))
print(f"Total Capacity: {total_capacity} slots")
print(f"Tasks per Node: {tasks_per_node}")
print(f"Tasks remaining for manual queue: {leftover_tasks}")