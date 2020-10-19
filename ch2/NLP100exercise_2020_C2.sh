#!/bin/bash

#10. Line count
#Count the number of lines of the file. Confirm the result by using wc command.

wc -l popular-names.txt | cut -f1 -d' '

#11. Replace tabs into spaces
#Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.

cat popular-names.txt | tr '\t' ' ' > popular-names.txt

#12. col1.txt from the first column, col2.txt from the second column
#Extract the value of the first column of each line, and store the output into col1.txt. Extract the value of the second column of each line, and store the output into col2.txt. Confirm the result by using cut command.

cat popular-names.txt | cut -f1 -d' ' > col1.txt
cat popular-names.txt | cut -f2 -d' ' > col2.txt

#13. Merging col1.txt and col2.txt
#Join the contents of col1.txt and col2.txt, and create a text file whose each line contains the values of the first and second columns (separated by tab character) of the original file. Confirm the result by using paste command.

paste col[1-2].txt > joint.txt

#14. First N lines
#Receive a natural number $N$ from a command-line argument, and output the first $N$ lines of the file. Confirm the result by using head command.

head --line=$1 popular-names.txt

#15. Last N lines
#Receive a natural number $N$ from a command-line argument, and output the last $N$ lines of the file. Confirm the result by using tail command.

tail --line=$1 popular-names.txt

#16. Split a file into N pieces
#Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries. Confirm the result by using split command.

split --number=$1 popular-names.txt

#17. Distinct strings in the first column
#Find distinct strings (a set of strings) of the first column of the file. Confirm the result by using cut, sort, and uniq commands.

cut -f1 -d$'\t' popular-names.txt | sort | uniq

#18. Sort lines in descending order of the third column
#Sort the lines in descending numeric order of the third column (sort lines without changing the content of each line). Confirm the result by using sort command.

sort -r -k 3 -t $'\t' popular-names.txt

#19. Frequency of a string in the first column in descending order
#Find the frequency of a string in the first column, and sort the strings by descending order of their frequencies. Confirm the result by using cut, uniq, and sort commands.

cut -f1 -d$' ' popular-names.txt | sort | uniq -c | sort -r