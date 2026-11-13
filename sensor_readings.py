#Average, Minimum, Maximum and count of sensor readings

Readings = [22,24,26,28,30]

count = len(Readings)
Min = min(Readings)
Max = max(Readings)

total = sum(Readings)
Avrg = total/count

print("Count:", count)
print("Minimum:", Min)
print("Maximum:", Max)
print(f"Average: {Avrg:.1f}")
