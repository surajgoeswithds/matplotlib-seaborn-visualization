#Assignment:Create a pie chart showing the market share of mobile OS (Android, iOS, others). Then recreate the same using a horizontal bar chart and observe which is easier to understand.
import matplotlib.pyplot as plt
plt.style.use("ggplot")

Operatingsystems = ['Android' , 'IOS' , 'Others']
usages = [72 , 27 , 1]

plt.pie(usages , labels=Operatingsystems , autopct='%1.1f%%', startangle=90)
plt.title("OS USAGES")
plt.show()

plt.barh(Operatingsystems , usages)
plt.show()