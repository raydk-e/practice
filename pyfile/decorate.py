import pandas as pd

def log_shape(func):
    def wrapper(df, *args, **kwargs):
        print (f"before transformation shape is {df.shape}")
        result = func(df,*args, **kwargs)
        print (f"after transformation shape is {result.shape}")
        print(result)
    return wrapper

@log_shape
def drop_missing (df):
    return df.dropna()

data = {
    "name": ["Kachana", "bebina", None, "Roga"],
    "age" : [25,None, 28, 32]
}

df = pd.DataFrame(data)

clean_df = drop_missing(df)

