# XAPID
Toward explainable Windows API-based malware detection

## File descriptions
### Header files
* windowsHeaders.csv contains the names of all of the header files listed on https://learn.microsoft.com/en-us/windows/win32/api/ as of 4/16/2025
* hardwareHeaders.csv contains the names of all of the header files listed on https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/_kernel/ as of 4/16/2025

### Collector script
* functionCollector.py scrapes info from the two URLs mentioned above, on all the header files listed in the above CSV files, to generate the output file documentedFunctions.txt

### Function databases
* documentedFunctions.txt contains function names, descriptions, parent header files, and documentation links of 19,047 functions
* supplementalFunctions.txt contains function names, descriptions, parent header files, and documentation links to 41 additional functions from https://ntdoc.m417z.com/

## References
* Documented Windows API calls were pulled from https://learn.microsoft.com/en-us/windows/win32/api/ and https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/_kernel/ on 4/16/2025
* Community documentation from https://ntdoc.m417z.com/ was used to create the supplemental functions list on 4/16/2025
