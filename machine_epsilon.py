# TODO
def machine_epsilon():
    epsilon = 1.0
    
    while 1.0 + epsilon > 1.0:
        epsilon_last = epsilon
        epsilon /= 2
        
    return epsilon_last

epsilon = machine_epsilon()
print(f"マシンイプシロン{epsilon}")