def optimize_delivery_schedule(packages):
    # Simulação de otimização de cronograma
    optimized_schedule = sorted(packages, key=lambda x: x['priority'])
    return optimized_schedule