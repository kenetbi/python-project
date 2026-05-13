colombian_pesos = float(input("What do you have left in pesos? ")) # 0.00028 in dollar
peruvian_soles = float(input("What do you have left in soles? ")) # 0.29 in dollar
brazilian_reais = float(input("What do you have left in reais? ")) # 0.20 in dollar

colpesos_to_dollar = colombian_pesos * 0.00028
persoles_to_dollar = peruvian_soles * 0.29
brazreais_to_dollar = brazilian_reais * 0.20

total_usd = colpesos_to_dollar + persoles_to_dollar + brazreais_to_dollar

print(f"The total USD you have is {total_usd}")