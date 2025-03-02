import math as m

# 
def powerInput(slope, strickler):

  p = 980   # density in kg/m³
  g = 9.81  # acceleration in m/s²
  h = 1.53  # hight of water column in m
  e = 0.1   # coefficient of efficiency
  r = h     # hydraulic radius ^2/3

  i = slope     # slope Excel in sheet convert to decimal number ^1/2
  k = strickler # strickler - coefficient in Excel sheet

  result = (p * g * h * i) * (k * m.pow(r , 2/3) * m.pow(i , 1/2)) * e 
  
  return result

# 
def main():

  print("----- Min of Power input -----")
  slope = float(input("Enter slope min from Excel: "))
  strickler = float(input("Enter Strickler min from Excel: "))
  w_eff = powerInput(slope, strickler)
  print(f"Result of power input min: {w_eff:.2f} w/m² \n")

  print("----- Max of Power input -----")
  slope = float(input("Enter slope max from Excel: "))
  strickler = float(input("Enter Strickler max from Excel: "))
  w_eff = powerInput(slope, strickler)
  print(f"Result of power input max: {w_eff:.2f} w/m² \n")

main()