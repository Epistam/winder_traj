z_far_end = 23.00
print(str(z_far_end).replace('.',','))



for i in range(20) :
    current_slice_fwd = f'''G1 Z{i} ''' # Format like 150,00

    print(current_slice_fwd)
   
coords = [{'x': a, 'y': a} for a in range(10)] 

print(coords)
