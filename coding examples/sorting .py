"""
list in the nested dictionary sorting
"""
stu_marks = [{"name": "siva", "marks": 10}, {"name": "rams", "marks": 20},
             {"name": "reddy", "marks": 500}]

# using sorted function it will sort the program
# using lambda based on keys
stu_marks = sorted(stu_marks, key=lambda l: l["marks"], reverse=False)
print stu_marks

stur_marks1= sorted(stu_marks, key=lambda l:l["name"], reverse=False)
print stur_marks1
