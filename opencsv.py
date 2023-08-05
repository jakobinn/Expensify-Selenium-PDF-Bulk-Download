import pandas as pd
from datetime import datetime
import urllib.request
import os
from urllib.parse import urlparse

def getReceiptData(filename = "receipts.csv"):
    data = pd.read_csv(filename)
    return data.values

def handleReceiptData(data = []):
    receipts = getReceiptData("receipts.csv")
    for row in receipts:
        if(row.size > 7):
            date = getDate(row)
            name = getName(row)
            price = getPrice(row)
            currency = getCurrency(row)
            link = getLink(row)
            print("Date:", date, "Name:", name, "Price:", price, "Currency:", currency, "Link:", link)


def fixAMDate (date = ""):
    # convert it into datetime object
    if(date != ""):
        dt_obj = datetime.strptime(date, '%d-%m-%Y')
        return dt_obj.strftime('%Y-%m-%d')
    else:
        return ""

def getDate(line = []):
    dateTemp = line[0]
    if(dateTemp != ""):
        date_object = datetime.strptime(dateTemp, '%Y-%m-%d %H:%M:%S')
        # Convert the datetime object back into a string, in the new format
        new_date_string = date_object.strftime('%d-%m-%Y')
        return new_date_string
    else:
        return ""

def getName(line = []):
    nameTemp = line[1]
    return nameTemp

def getPrice(line = []):
    priceTemp = line[2]
    if priceTemp and priceTemp.endswith('.00'):
        price = priceTemp[:-3]
        price = price.replace(',', '')
        price = price.replace('.', '')
        return price
    else:
        price = price.replace(',', '')
        price = price.replace('.', '')
        return priceTemp

def getCurrency(line = []):
    nameTemp = line[8]
    return nameTemp

def getLink(line = []):
    if line.size < 11:
        return ""
    else:
        return line[10]

def getPDFFileName(line = []):
    return getDate(line) + "_" + getName(line) + "_" + getPrice(line) + "_" + getCurrency(line)


def getFileType(url = ""):
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]    
    if ext == '.pdf':
        return ".pdf"
    elif ext == '.jpg':
        return ".jpg"
    elif ext == '.jpeg':
        return ".jpeg"
    elif ext == '.png':
        return ".png"
    else:
        return ".pdf"


# def downloadPDF(path, line = []):
#     filename = getPDFFileName(line)
#     print(filename)
#     filepath = path + filename
#     if os.path.isfile(filepath):
#         print("File already exists")
#         return
#     else:
#         link = getLink(line)
#         print("File already exists")
#         sleep(3)
#         urllib.request.urlretrieve(link, filepath)
#         return


# data = pd.read_csv('receipts.csv')

# # If you still want it as a numpy array, you can convert it
# numpy_array = data.values
# print(numpy_array)