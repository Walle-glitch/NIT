#
#
#
#
intakt_idag =float(input('intäkt idag:  '))
ranta_y = float(5)
ranta = float((1 + 0.045) ** ranta_y)
present_Value = intakt_idag / ranta

print(f'framtida värdet på {intakt_idag:.0f} om {ranta_y:.0f} år är: {present_Value:.2f} kr ')


