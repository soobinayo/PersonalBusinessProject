echo "# Personal-Business-Project" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/soobinayo/Personal-Business-Project.git
git push -u origin master

import sys
import os
import matplotlib
import matplotlib.pyplot as plot
import matplotlib.dates as matdate
import datetime

def readDate(in_line):
    index = in_line[1].find('(')
    index_end = in_line[1].find(')')
    index = int(index) + 1
    index_end = int(index_end) - 9
    date = in_line[1][index:index_end]
    data_list["Dates"].append(date)
    
def readCash(in_line):
    index = in_line[20].find('$')
    index_end = in_line[20].find('n')
    index = int(index) + 1
    index_end = int(index_end)
    cash = in_line[20][index:index_end]
    data_list["Cash"].append(cash)

def readCreditCard(in_line):
    index = in_line[22].find('$')
    index_end = in_line[22].find('n')
    index = int(index) + 1
    index_end = int(index_end)
    creditcard = in_line[22][index:index_end]
    data_list["CreditCard"].append(creditcard)

def readInvoiceDrop(in_line):
    index = in_line[61].find(':')
    index_end = in_line[61].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    invoicedrop = in_line[61][index:index_end]
    data_list["InvoiceDrop"].append(invoicedrop)

def readDryDrop(in_line):
    index = in_line[64].find(':')
    index_end = in_line[64].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    drydrop = in_line[64][index:index_end]
    data_list["DryDrop"].append(drydrop)

def readLaundryDrop(in_line):
    index = in_line[66].find(':')
    index_end = in_line[66].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    laundrydrop = in_line[66][index:index_end]
    data_list["LaundryDrop"].append(laundrydrop)

def readAlterationDrop(in_line):
    index = in_line[67].find(':')
    index_end = in_line[67].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    alterationdrop = in_line[67][index:index_end]
    data_list["AlterationDrop"].append(alterationdrop)

def readInvoicePick(in_line):
    index = in_line[71].find(':')
    index_end = in_line[71].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    invoicepick = in_line[71][index:index_end]
    data_list["InvoicePick"].append(invoicepick)

def readDryPick(in_line):
    index = in_line[74].find(':')
    index_end = in_line[74].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    drypick = in_line[74][index:index_end]
    data_list["DryPick"].append(drypick)

def readLaundryPick(in_line):
    index = in_line[76].find(':')
    index_end = in_line[76].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    laundrypick = in_line[76][index:index_end]
    data_list["LaundryPick"].append(laundrypick)

def readAlterationPick(in_line):
    index = in_line[77].find(':')
    index_end = in_line[77].find('$')
    index = int(index) + 2
    index_end = int(index_end) - 1
    alterationpick = in_line[77][index:index_end]
    data_list["AlterationPick"].append(alterationpick)

def showGraph(yaxis, value):
    dates = [datetime.datetime.strptime(d, '%m/%d/%Y').date() for d in data_list["Dates"]]
    plot.gca().xaxis.set_major_formatter(matdate.DateFormatter('%m/%d/%Y'))
    plot.gca().xaxis.set_major_locator(matdate.DayLocator())
    plot.xlabel("Time")
    plot.ylabel(yaxis)
    plot.plot(dates, value)
    plot.show()

data_list = {"Dates":[], "Cash":[], "CreditCard":[], 
             "InvoiceDrop":[], "DryDrop":[], "LaundryDrop":[], "AlterationDrop":[], 
             "InvoicePick":[], "DryPick":[], "LaundryPick":[], "AlterationPick":[]}

for year in range(2017,2019):
    for month in range(1,13):
        for day in range(1,32):
            if month <= 9:
                if day <= 9:
                    filelocation = 'C:\data\Report0' + str(month) + '-0' + str(day) + '-' + str(year) + '.txt'
                else:
                    filelocation = 'C:\data\Report0' + str(month) + '-' + str(day) + '-' + str(year) + '.txt'
            else:
                if day <= 9:
                    filelocation = 'C:\data\Report' + str(month) + '-0' + str(day) + '-' + str(year) + '.txt'
                else:
                    filelocation = 'C:\data\Report' + str(month) + '-' + str(day) + '-' + str(year) + '.txt'
            if not os.path.exists(filelocation):
                pass
            else:
                with open(filelocation, 'rt') as fileOpen:
                    in_line = fileOpen.readlines()[:]
                    readDate(in_line)
                    readCash(in_line)
                    readCreditCard(in_line)
                    readInvoiceDrop(in_line)
                    readInvoicePick(in_line)
                    readDryDrop(in_line)
                    readDryPick(in_line)
                    readLaundryDrop(in_line)
                    readLaundryPick(in_line)
                    readAlterationDrop(in_line)
                    readAlterationPick(in_line)

yaxis = input('Enter which data you want to see (cash in, cc in, invoice dropoff, invoice pickup: ')
if yaxis == 'cash in':
    value = data_list["Cash"]
    yaxis = "Cash ($)"
elif yaxis == 'cc in':
    value = data_list["CreditCard"]
    yaxis = "Credit Card ($)"
showGraph(yaxis, value)
