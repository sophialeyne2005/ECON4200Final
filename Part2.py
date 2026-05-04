mean_close = daily.mean()
mean_close

std_close = daily.std()
std_close

mean_value = mean_close.iloc[0]
std_value = std_close.iloc[0]

print("Mean daily close:", mean_value)
print("Standard deviation:", std_value)