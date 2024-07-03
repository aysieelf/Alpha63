lp_w = int(input())
lp_h = int(input())
sp_w = int(input())
sp_h = int(input())

fits = []
if sp_w <= lp_w and sp_h <= lp_h:
    w_counts = lp_w // sp_w
    h_counts = lp_h // sp_h
    temp_fit = w_counts * h_counts
    fits.append(temp_fit)

if sp_w <= lp_h and sp_h <= lp_w:
    w_counts = lp_w // sp_h
    h_counts = lp_h // sp_w
    temp_fit = w_counts * h_counts
    fits.append(temp_fit)

max_fit = max(fits)
print(max_fit)