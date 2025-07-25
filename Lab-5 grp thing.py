DSci = {"Anil", "Bhavya", "Chetan", "Deepa"}
CComp = {"Chetan", "Deepa", "Eshan", "Farah"}

both_courses = DSci.intersection(CComp)
print("Students in both courses:", both_courses,"\n")

only_one_course = DSci.symmetric_difference(CComp)
print("Students in only one course:", only_one_course,"\n")

unique_students = DSci.union(CComp)
print("Total unique students:", len(unique_students),"\n")

DSci.intersection_update(CComp)
print("Updated DSci set:", DSci)
