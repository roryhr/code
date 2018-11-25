Title:  Code for Tomorrow
Date:   2018-04-02
Tags: python, miniessays

This is the first of a series of short articles.

# Code for Tomorrow

How do you know if your code is good? 
This is subjective, to be sure, but is clarified by answering a given question which sets the standard by which the code is judged.
The most question being “Does it work?” 
Then you hear “Is it fast?” Is it tested? How is it used?


I add to this list, “Imagine that five years from now someone comes upon your code. Can they use it? Will it work?” Whenever I’m coding this is in the back of my mind.


Consider, the average tenure in tech is 2-3 years so five years is two generations of employees; nobody who originally wrote the code is around. 
The wiki pages were archived and lost and the Jira stories are gone because everyone is using something much better now. 
Yet your code sits and is one day discovered, perfectly preserved like Pompeii. 


The code should be self-documenting. 
Not as in readable but in the documentation should literally live with the code.
If someone cloned your git repo they should also have the documentation. 
If they found your Oracle database then all columns and tables should be described using the builtin comment and metadata features.


Our imaginary employee from the future will try run the code. 
Does it rely on deprecated packages? Open source packages come and go. Recognize fads and use packages that will be around.


What will our future person want to know? Does it work? Is it correct? That’s where tests come in. They give confidence to the newcomer that the code is correct, that timezones are handled correctly.


The last thing is readability. You want it to be simple and timeless so someone who stumbles upon it can figure out how it works.


All of these good things come from considering your code five years from now.
