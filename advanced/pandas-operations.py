import pandas as pd

name_and_ages = {"name": ["Berkay", "Gediz", "Berkay", "Gediz"],
                 "age": [25, 25, 25, 25]}

data = pd.DataFrame(name_and_ages)
print(data)
