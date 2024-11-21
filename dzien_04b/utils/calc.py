def bmi(masa: float, wzrost: float) -> float:
    try:
        if wzrost > 3:
            wzrost = wzrost / 100
        bmi = masa / wzrost**2
        return bmi

    except Exception as error:
        print("Błąd:", error)
        return -1
