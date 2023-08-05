# Expensify PDF Bulk Exporter

## This code uses Selenum to export PDF files in bulk from Expensify based on DATE_FROM and DATE_TO in the prog_settings.py file. 

### To use, you need to do the following

1. Download Selenium Chrome driver
2. Install relevant packages with pip (seen in the import statements in opencsv.py and getpdfs.py)
3. Update prog_settings_template with relevant values and change the name to prog_settings.py.
4. Make sure the default.csv template in Expensify has not been changed.
5. Run it. :)