sales = [1200,1300,560,4500,2100]
tot = 0
avg =0
for x in sales:
    tot = tot + x
print(f"Total sales {tot}")
avg = tot/len(sales)
print(f"Average Sales {avg}")
print(f"Highest sales {max(sales)}")
print(f"Lowest sales {min(sales)}")