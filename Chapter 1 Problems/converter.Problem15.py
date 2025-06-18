 

# Conversion constants (correctly named for clarity)
KG_TO_LBS = 2.20462  # 1 kg = 2.20462 lbs
LBS_TO_KG = 0.453592  # 1 lb = 0.453592 kg

def kg_to_lbs(kg):
    return kg * KG_TO_LBS

def lbs_to_kg(lbs):
    return lbs* LBS_TO_KG

print(kg_to_lbs(4))
print(lbs_to_kg(9))