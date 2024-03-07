#import test

slice_string = """[Pass {pass_no} : Slice {slice_no}]
G1 Z150,00 R4,53 B35,00 [Move Far End]
G4 L601 C724,29 R4,53 B0,00 [Dwell Far End]
G1 Z100,00 R4,53 B-35,00 [Move Home End]
G4 L602 C728,57 R4,53 B0,00 [Dwell Home End]"""

#z_far_end = str(23.00).replace('.', ',')
#r_next = str(23.00).replace('.', ',')
#
#current_slice_fwd = f'''G1 Z{z_next} R{r_next} B35,00 [Slice {slice_no}]
#G4 L601 C{c_next} R{r_next} B0,00 [Dwell Far End]''' # Format like 150,00
#
#current_slice_bwd = f'''G1 Z{z_next} R{r_next} B35,00 [Slice {slice_no}]
#G4 L601 C{c_next} R{r_next} B0,00 [Dwell Far End]''' # Format like 150,00
#
#dwell_far_end = 'G4 L601 C{theta_far_end} R{r_next} B0,00 [Dwell Far End]' # Format like 150,00
#move_home_end = 'G1 Z{z_home_end} R{r_next} B-35,00 [Move Far End]' # Format like 150,00
#dwell_home_end = 'G4 L601 C{theta_home_end} R{r_next} B0,00 [Dwell Far End]' # Format like 150,00

#def write_slice(pass_no, slice_no) :
#
#def write_pass(pass_no)
#
#
#gabh = move_far_end.format(
#    z_far_end=,
#    r_next=,
#    theta_far_end=,
#    z_home_end=,
#    theta_home_end,
#)
#
#print(pass_string)


# dummy coords
coords = [{'z': float(a), 'c': float(a), 'r': float(a)} for a in (list(range(100,110)) + list(reversed(range(100,110))))]

# GCode strings
gcode = []

pass_no = 0

# Refreshed values
r_next = 0
slice_no = 0
c_next = 0
z_next = 0

# Formattable string
slice_string = '[Slice {}]\nG1 Z{} R{} B35,00\nG4 L601 C{} R{} B35,00\n'
dwell_string = 'G4 L602 C{} R{} B0,00\n'

gcode.append(f'[===========================> PASS {pass_no} START]\n')

# from home to far end
gcode.append('[===========================> Travelling from home to far end]\n')
for i, c in enumerate(coords) :
    # Beginning of slice : set target coords
    z_next = c['z']
    c_next = c['c']
    r_next = c['r']
    slice_no = i

    # Put coords in the command
    current_slice = slice_string.format(slice_no, 
                                        "{:.2f}".format(c['z']).replace('.', ','), r_next, 
                                        "{:.2f}".format(c['c']).replace('.', ','), r_next)
    gcode.append(current_slice)

# dwell at far end
current_dwell = dwell_string.format(c_next, r_next)
c_next += 360 + 180
gcode.append('[===========================> Dwelling at far end]\n')
gcode.append(current_dwell)

# from far end to home
gcode.append('[===========================> Travelling from far end to home]\n')
for i, c in enumerate(reversed(coords)) :
    # Beginning of slice : set target coords
    z_next = c['z']
    c_next = c['c']
    r_next = c['r']
    slice_no = len(coords) - i - 1
    
    # Put coords in the command
    current_slice = slice_string.format(slice_no, 
                                        "{:.2f}".format(c['z']).replace('.', ','), r_next, 
                                        "{:.2f}".format(c['c']).replace('.', ','), r_next)
    gcode.append(current_slice)

# dwell at home
current_dwell = dwell_string.format(c_next, r_next)
c_next += 360 + 180
gcode.append('[===========================> Dwelling at home]\n')
gcode.append(current_dwell)

gcode.append(f'[===========================> PASS {pass_no} DONE]\n')


f = open('test.X4G', 'w')
f.writelines(gcode)
f.close()
