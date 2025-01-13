# bmi calculator - Codewars:
def bmi(height,weight):
    bm_calculate = weight/(height **2)
    if bm_calculate <= 18.5:
        return "Underweight"
    elif bm_calculate <= 25.0:
        return "Normal"
    elif bm_calculate <= 30.0:
        return "Overweight"
    elif bm_calculate > 30:
        return "Obese"