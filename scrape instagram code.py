import time
import random
try: 
    from googlesearch import search
except ImportError:  
    print("No module named 'google' found") 

# what to search (replace X)
queries =['site:instagram.com "X"']

with open("urls.txt", "w+") as f:
    #f.write("\nlink\n")
    for query in queries:
        for j in search(query, lang='en', pause=10):
            time.sleep(35)
            print('found: ',j)
            f.write(j)
            f.write("\n")
