0x06. Regular expression

0. Simply matching School
The regular expression must match School

1. Repetition Token #0
for instance match hbttn,  hbtttn,  hbttttn,  hbtttttn, but don't match  hbtn and  hbn

2. Repetition Token #1
match hbt, hbtn but dont match hbbtn and hbbbtn

3. Repetition Token #2
match hbtn, hbttn, hbtttn but not hbn

4. Repetition Token #3
match hbn, hbtn, hbttn, hbtttn but not hbon

5. Not quite HBTN yet
match strings that start with h and end with n

6. Call me maybe
match 10 digit phone number

7. OMG WHY ARE YOU SHOUTING?
match capital letters

8. Textme
Your script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used
