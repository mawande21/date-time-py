from datetime import datetime, timedelta

today = datetime.today()

#print 10 days ,two weeks apart
for d in range(10):
    new_date = today + timedelta(days=14)
    today = new_date
    print(today.strftime("%Y :%m : %d"))
