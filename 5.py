from datetime import datetime

# The Moscow Times
date_str1 = "Wednesday, October 2, 2002"
datetime1 = datetime.strptime(date_str1, "%A, %B %d, %Y")
print(datetime1)

# The Guardian
date_str2 = "Friday, 11.10.13"
datetime2 = datetime.strptime(date_str2, "%A, %d.%m.%y")
print(datetime2)

# Daily News
date_str3 = "Thursday, 18 August 1977"
datetime3 = datetime.strptime(date_str3, "%A, %d %B %Y")
print(datetime3)