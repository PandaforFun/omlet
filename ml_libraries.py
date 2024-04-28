import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data provided by the user
subjects = ['Math', 'Science', 'History', 'English', 'Computer Science']
marks = [90, 85, 88, 92, 95]

# NumPy implementation
np_marks = np.array(marks)

print("NumPy Array:")
print(np_marks)

# Pandas implementation
data = {'Subjects': subjects, 'Marks': marks}
df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# Matplotlib implementation
plt.bar(subjects, marks, color='skyblue')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Subject-wise Marks')
plt.xticks(rotation=45)
plt.show()
