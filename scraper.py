f = open("html.txt","r")
prev_line = ""
thedic = {}
for line in f.readlines():
  if "data-title=\"State\"" in line:
    #88-90 is state
    if line[88:90] == "MI":
      end_of_city = prev_line.find("<",88)
      if prev_line[87:end_of_city] not in thedic:
        thedic[prev_line[87:end_of_city]] = 1
      else:
        thedic[prev_line[87:end_of_city]] += 1


  prev_line = line

for w in sorted(thedic, key=thedic.get, reverse=True):
  print(w, thedic[w])
