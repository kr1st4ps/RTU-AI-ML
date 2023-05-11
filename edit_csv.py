import pandas as pd

df = pd.read_csv('6_class_stars.csv',sep=',',encoding='latin-1' )

#   Assign actual string values of star types
df.loc[df['Star type'] == 0, "Star type"] = "Brown Dwarf"
df.loc[df['Star type'] == 1, "Star type"] = "Red Dwarf"
df.loc[df['Star type'] == 2, "Star type"] = "White Dwarf"
df.loc[df['Star type'] == 3, "Star type"] = "Main Sequence"
df.loc[df['Star type'] == 4, "Star type"] = "Supergiant"
df.loc[df['Star type'] == 5, "Star type"] = "Hypergiant"

#   Fixed misspelled colors
df.loc[df['Star color'] == "Blue white", "Star color"] = "Blue White"
df.loc[df['Star color'] == "Blue white ", "Star color"] = "Blue White"
df.loc[df['Star color'] == "Blue-white", "Star color"] = "Blue White"
df.loc[df['Star color'] == "Blue-White", "Star color"] = "Blue White"
df.loc[df['Star color'] == "Blue ", "Star color"] = "Blue"
df.loc[df['Star color'] == "Yellowish White", "Star color"] = "Yellow White"
df.loc[df['Star color'] == "White-Yellow", "Star color"] = "Yellow White"
df.loc[df['Star color'] == "yellow-white", "Star color"] = "Yellow White"
df.loc[df['Star color'] == "Pale yellow orange", "Star color"] = "Yellow Orange"
df.loc[df['Star color'] == "Orange-Red", "Star color"] = "Orange Red"
df.loc[df['Star color'] == "white", "Star color"] = "White"
df.loc[df['Star color'] == "Whitish", "Star color"] = "White"
df.loc[df['Star color'] == "yellowish", "Star color"] = "Yellow"
df.loc[df['Star color'] == "Yellowish", "Star color"] = "Yellow"


df.to_csv('stars.csv', sep=',', index=False)