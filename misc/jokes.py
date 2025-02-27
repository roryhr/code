"""If one joke is good then 100 is better

This was prompted by the question, "Are LLMs deterministic?
The short answer is "no". But, as you can see, the joke is the same -- 
so it sort of it deterministic. 

Usage
python misc/jokes.py
"""

import subprocess
import multiprocessing
import collections

import pandas as pd

NUM_RUNS = 100


def get_joke(_):
    result = subprocess.run(
        ["ollama", "run", "gemma2:latest", "tell me a joke"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


if __name__ == "__main__":
    with multiprocessing.get_context("spawn").Pool(processes=5) as pool:
        results = pool.map(get_joke, range(NUM_RUNS))

    counter = collections.Counter(results)
    unique_jokes = len(counter)
    most_common = counter.most_common(5)

    print(f"\nTotal Unique Jokes: {unique_jokes}")
    print(f"Most Common Jokes:\n")
    for joke, count in most_common:
        print(f"{count} times: {joke}\n")

    print("Pandas Checks\n\n")
    df = pd.DataFrame(results)
    print(df.describe())
    print(df.value_counts())

# Total Unique Jokes: 42
# Most Common Jokes:

# 12 times: Why don't scientists trust atoms?

# Because they make up everything! 😄

# 10 times: Why don't scientists trust atoms?

# Because they make up everything! 😄

# 9 times: Why don't scientists trust atoms?

# Because they make up everything!  😄

# 8 times: Why don't scientists trust atoms?

# Because they make up everything! 😄


# Let me know if you want to hear another one! 😊

# 6 times: Why don't scientists trust atoms?

# Because they make up everything! 😊

# Pandas Checks


#                                                         0
# count                                                 100
# unique                                                 42
# top     Why don't scientists trust atoms?\n\nBecause t...
# freq                                                   12
# 0
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😄                                                              12
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😄                                                             10
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😄                                                             9
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😄  \n\n\nLet me know if you want to hear another one! 😊         8
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😊                                                              6
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😜                                                               5
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😊                                                               4
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😄  \n\n\nLet me know if you want to hear another one! 😊        3
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😜                                                             3
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😄  \n\n\nLet me know if you want to hear another one!           3
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😄  \n\n\nLet me know if you'd like to hear another one! 😊       3
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😄  \n\n\nLet me know if you want to hear another one!          2
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😜  \n\n\nLet me know if you want to hear another one! 😊         2
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😄  \n\n\nLet me know if you'd like to hear another one! 😊      2
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😜  Let me know if you'd like to hear another one!  🚀          1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😜  \n\n\nLet me know if you want to hear another one! 😊       1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  🧪😂                                                            1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  🧪 😄  \n\n\nLet me know if you want to hear another one! 😊     1
# Why don't scientists trust atoms?\n\nBecause they make up everything!  🔬 😄                                                            1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  🧪😂  Let me know if you want to hear another one! 😄            1
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😄  \n\n\nLet me know if you'd like to hear another one!        1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😄  \n\n\nLet me know if you want to hear another one! 😊       1
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😊  \n\n\nLet me know if you want to hear another one!  😄       1
# Why don't scientists trust atoms? \n\nBecause they make up everything! 😜                                                              1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😄  \n\n\nLet me know if you'd like to hear another one! 😊     1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😁                                                             1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😄  \n\n\nLet me know if you want to hear another one! 😄       1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  😄  \n\n\nLet me know if you want to hear another one!         1
# Why don't scientists trust atoms?\n\nBecause they make up everything!  😂                                                              1
# Why don't scientists trust atoms? \n\nBecause they make up everything!  🔬 😂                                                           1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 🧪😜  \n\n\nLet me know if you want to hear another one! 😄        1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 🧪😄  \n\n\nLet me know if you'd like to hear another one! 😊      1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 🧪 😄  \n\n\nLet me know if you'd like to hear another one! 😊     1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 🧪 😄  \n\n\nLet me know if you want to hear another one! 😊       1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😜  Let me know if you want to hear another one! 😊               1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😜  Let me know if you want to hear another one! 😄               1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😜  \n\n\nLet me know if you'd like to hear another one! 😄       1
# Why don't scientists trust atoms?\n\nBecause they make up everything! 😜  \n\n\nLet me know if you want to hear another one! 😄         1
# Why don't scientists trust atoms?\n\nBecause they make up everything!  😜                                                              1
# Why don't scientists trust atoms?\n\nBecause they make up everything!  😄  \n\n\nLet me know if you want to hear another one! 😊        1
# Why don't scientists trust atoms?\n\nBecause they make up everything!  😄                                                              1
# Why don't scientists trust atoms? \n\nBecause they make up everything! 🧪  😄                                                           1
