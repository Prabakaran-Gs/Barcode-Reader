import csv  
def insertval(details):
    lib_file=open("Database.csv",'a+')
    indices=["SI.NO","STUDENT ID","DATE","IN_TIME","EXIT_TIME"]
    writer=csv.writer(lib_file)
    if details[0]==1:
        writer.writerow(indices)
    writer.writerow(details)


