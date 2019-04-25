subjects=["I","YOU"]
verbs=["love","play"]
objects=["hocky","boofsfs"]

for i in range(len(subjects)):
               for j in range(len(verbs)):
                              for k in range(len(objects)):
                                  sentence="%s%s%s" %(subjects[i],verbs[j],objects[k])

                              print sentence
                                  
