import pandas as pd
import time

def time_taken(func):
    def wrapper(df, *args, **kwargs):
        start=time.time()
        result= func(df, *args, **kwargs)
        end = time.time()
        print(f"time taken {end-start: .4f} seconds")
        return result
    return wrapper

@time_taken
def sort_by_column(df, col):
    return df.sort_values(by=col)

data = {
    "Name": ["Rabi", "Kanika", "Bijuli", "Kamala"],
    "Age": [73,34,45,32]
}

df = pd.DataFrame(data)

sorted_df = sort_by_column(df, "Age")
print(sorted_df)
