
# %%
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from pathlib import Path
import re

url = "https://unicode.org/emoji/charts/full-emoji-list.html"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

OUTPUT_DIR = str(Path.cwd()) + "/emojis.csv"

table_rows = soup.find_all('tr')

def combine_codes(code):
    # convert codes to string and convert to correct format
    code_list = code.split("+")
    emoji_code = code_list[-1]
    length = len(emoji_code)
    diff = int(8 - length)
    zeros = str("0" * diff)
    return "\\U" + zeros + emoji_code

# create dictionary to store values
data = {"code": [],
        "name": []}

# iterate through rows in <tr>
for rows in table_rows:
    # get lists of all the <td> with class of "code" or "name"
    emoji_codes = rows.find_all(class_="code")
    emoji_names = rows.find_all(class_="name")

    for code in emoji_codes:
        unicode = str(code.text)
        code_list = unicode.split(" ")
        emoji_code = "".join(list(map(combine_codes, code_list)))

        data["code"].append(emoji_code)

    for name in emoji_names:
        # convert names to strings, remove ⊛ symbols and reformat certain emojis (e.g. family and flags)
        emoji_name = str(name.text)

        if emoji_name[0] == "⊛":
            emoji_name = emoji_name[2:]

        emoji_name = emoji_name.replace(" ", "_")
        emoji_name = emoji_name.replace(":", "")
        emoji_name = emoji_name.replace(",", "")
        emoji_name = emoji_name.replace("\"", "")
        emoji_name = emoji_name.replace("flag_", "")
        emoji_name = emoji_name.replace("o clock", "")
        emoji_name = emoji_name.replace(" s ", "s ")

        # emoji_name = emoji_name.replace("’", "")
        # emoji_name = emoji_name.replace(".", "")
        # emoji_name = emoji_name.replace("-", "_")
        # emoji_name = emoji_name.replace("“", "_")
        # emoji_name = emoji_name.replace("”", "_")

        data["name"].append(emoji_name.lower())

df = pd.DataFrame(data=data)
df.head()

# df.to_csv(OUTPUT_DIR, index=False)
