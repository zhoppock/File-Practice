def tableOne(x):
  group1 = ""
  r = 0
  group1 += "      |Seat A|Seat B|\n"
  for f in x:
    group1 += "Row " + str(r) + " | "
    for c in f: 
      group1 += c + " | "
    r += 1
    group1 += "\n"
  return group1

def tableTwo(x):
  group2 = ""
  group2 += "      |Seat A|Seat B|Seat C|Seat B|\n"
  r = 0
  for o in x:
    group2 += "Row "+ str(r) + " | "
    for a in o: 
      group2 += a + " | "
    r += 1
    group2 += "\n"
  return group2