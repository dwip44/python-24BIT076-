for i in range(0,25):
    if i < 12:
        print(f"{i}:00 am ")
    if i > 12:
        print(f"{i}:00 pm ")
    if i == 12:
        print(f"Noon")
    if i == 24:
        print(f"Midnight")
