import pandas as pd
data = {
    "Name": ["Jasraj", "Diavnshi", "Kaashvi"],
    "Marks": [98, 95, 90]
}
df = pd.DataFrame(data)
print(df)
print("\nStudents with Marks above 80")
print(df[df["Marks"] > 80])
print("\nAverage Marks")
print(df["Marks"].mean())