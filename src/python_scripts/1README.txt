This folder contains all python scripts that I have used.
Note: The first scripts are a bit messy as I was playing with different options, further tables are more organised and more readible so I'd suggest following blueprint files

I have used openpyxl(only for xlsx files, doesnt work for xls) and xlrd(works for both xlsx/xls) to read excel files and put relevant rows/columns into lists, then I have used csv writer to write csv files.

I have saved ids(institution/local authority ids) in dictionaries and then I mapped them to relevant files to use them as foreign keys.
Local authority: ids are basically ecodes without E at the beginning - it might be needed in the future though so it might be worth changing it but mysql didnt let me use Strings as foreign keys and I haven't found a solution