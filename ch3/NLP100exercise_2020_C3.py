import json
import gzip

#20. Read JSON documents
#Read the JSON documents and output the body of the article about the United Kingdom. Reuse the output in problems 21-29.

def C3_20(keyword):
	with gzip.open('enwiki-country.json.gz', "r") as f:
		for line in f:
			json_load = json.loads(line)
			if json_load['title'] == keyword :
				json_target = json_load
				break
			if json_load['title'] == "":
				break
	return json_target

json_UK = C3_20("United Kingdom")
print(C3_20("United Kingdom")['text'])

import re

#21. Lines with category names
#Extract lines that define the categories of the article.

def C3_21(json_data):
	pattern = re.compile(r'^(\[{2}Category\:\s*.+?\s*\]{2})$',re.MULTILINE)
	return re.findall(pattern,json_data['text'])

json_UK_category = C3_21(json_UK)
print(json_UK_category)

#22. Category names
#Extract the category names of the article.

def C3_22(json_category):
	pattern = re.compile(r'^\[{2}Category\:\s*(.+?)\s*\]{2}$',re.MULTILINE)
	return [re.findall(pattern,category)[0] for category in json_category]
	
json_category_names = C3_22(json_UK_category)
print(json_category_names)

#23. Section structure
#Extract section names in the article with their levels. For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".

def C3_23(json_data):
	pattern = re.compile(r'^(={2,})\s*(.+?)\s*\1$', re.MULTILINE + re.VERBOSE)
	return re.findall(pattern,json_data['text'])
	
def C3_23_print(json_section):
	for section in json_section:
		level = len(section[0]) - 1
		print('{indent}{section}:{level}'.format(indent='\t'*level, section=section[1],level=level))

json_UK_section = (C3_23(json_UK))
C3_23_print(json_UK_section)

#24. Media references
#Extract references to media files linked from the article.



#25. Infobox
#Extract field names and their values in the Infobox “country”, and store them in a dictionary object.
#
#26. Remove emphasis markups
#In addition to the process of the problem 25, remove emphasis MediaWiki markups from the values. See Help:Cheatsheet.
#
#27. Remove internal links
#In addition to the process of the problem 26, remove internal links from the values. See Help:Cheatsheet.
#
#28. Remove MediaWiki markups
#In addition to the process of the problem 27, remove MediaWiki markups from the values as much as you can, and obtain the basic information of the country in plain text format.
#
#29. Country flag
#Obtain the URL of the country flag by using the analysis result of Infobox. (Hint: convert a file reference to a URL by calling imageinfo in MediaWiki API)