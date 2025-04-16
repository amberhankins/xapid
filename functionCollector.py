import requests
from bs4 import BeautifulSoup

def getFunctionsTable(url, headerFile):
    # Get content from docs website
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if header file has defined functions
    functions = soup.find(id='functions')
    if not functions:
        return (f"No functions: {url}.\n")

    # Check for functions table
    table = functions.find_next('table')
    if not table:
        return (f"No table: {url}.\n")

    # Get functions names, descriptions, and links from table
    rows = table.find_all('tr')
    output = []
    for row in rows:
        cells = row.find_all(['td', 'th'])
        if not cells:
            continue
        content = cells[0].text.strip().split(' ',1)
        name = content[0].replace(",", "")
        desc = content[-1].replace(",", "")
        link = cells[0].find('a')
        href = "https://learn.microsoft.com" + link['href'] if link else ''
        if "," in href:
            href = ''
        if name != '':
            output.append(f"{name},{desc},{headerFile},{href}\n")
    return output

def main():
    outfile = open("documentedFunctions.txt", "w", encoding="utf8")
    outfile.write("Function Name,Description,Header File,Docs Link\n")
    errorfile = open("Errors.txt", "w", encoding="utf8")

    file = open("windowsHeaders.csv", "r")
    headerFiles = file.read()
    headerFiles = headerFiles.split(",")
    for headerFile in headerFiles:
        headerFile = headerFile[:-2]
        url = (f"https://learn.microsoft.com/en-us/windows/win32/api/{headerFile}/")
        results = getFunctionsTable(url, headerFile)
        if headerFile in results[0]:
            for item in results:
                outfile.write(item)
    file.close()

    file = open("hardwareHeaders.csv", "r")
    headerFiles = file.read()
    headerFiles = headerFiles.split(",")
    for headerFile in headerFiles:
        headerFile = headerFile[:-2]
        url = (f"https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/{headerFile}/")
        results = getFunctionsTable(url, headerFile)
        if headerFile in results[0]:
            for item in results:
                outfile.write(item)
    file.close()

    outfile.close()
    errorfile.close()

if __name__ == "__main__":
    main()