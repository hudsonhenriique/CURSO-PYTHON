# %%
# Quais números são divisíveis por 4
# No intervalo [4-100]

count =4

while count <= 100:
    if count % 4 == 0:
        print(count)
    count += 1
# %%
for count in range(4, 101):
    if count % 4 == 0:
        print(count)