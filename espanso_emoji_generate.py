from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from pathlib import Path
import re
import json
import numpy as np
from pathlib import Path

url = "https://unicode.org/emoji/charts/full-emoji-list.html"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# shortcodes fetched from https://unpkg.com/emojilib@2.4.0/emojis.json
# from the package Emojilib found here https://github.com/muan/emojilib
shortcodes_df = pd.read_json('../emoji_shortcodes.json', orient='index')

CSV_OUTPUT_DIR = str(Path.cwd()) + "/emojis.csv"
PACKAGE_OUTPUT_DIR = str(Path.cwd()) + "package.yml"

table_rows = soup.find_all('tr')

### Functions

def combine_codes(code):
    # convert codes to string and convert to correct format
    code_list = code.split("+")
    emoji_code = code_list[-1]
    length = len(emoji_code)
    diff = int(8 - length)
    zeros = str("0" * diff)
    return "\\U" + zeros + emoji_code

def shortcode_cleanup(shortcode):
    shortcode = shortcode.replace("-", " ") # remove - (e.g. see-no-evil_monkey)
    shortcode = shortcode.replace(".", "") # remove . (e.g. mrs._claus)
    shortcode = shortcode.replace(":", "") # replace : (e.g. woman: blond hair)
    return shortcode

def convert_to_spaces(df, convert):
    for index in df.index:
        if convert == True:
            df.loc[index, "shortcode"] = df.loc[index, "shortcode"].replace("_", " ")
        elif convert == False:
            df.loc[index, "shortcode"] = df.loc[index, "shortcode"].replace(" ", "_")

def generate_yaml(df):
    # define yml elements
    matches = "matches:\n"
    trigger = "  - trigger: "
    replace = "\n    replace: "

    body = ""

    # iterate through df and add to output string
    for index, row in df.iterrows():
        name = row["shortcode"]
        code = row["unicode"]

        name = "\":" + name + ":\""
        code = "\"" + code + "\""

        emoji_item = trigger + name + replace + code + "\n"
        body = body + emoji_item

    yml_output = matches + body

    # save to yml file
    with open(PACKAGE_OUTPUT_DIR, "w") as f:
        f.write(yml_output)


### Fetching

# create dictionary to store values
data = {"unicode": [],
        "chars": [],
        "fullname": []}

# iterate through rows in <tr>
for rows in table_rows:
    # get lists of all the <td> with class of "code" or "name"
    emoji_codes = rows.find_all(class_="code")
    emoji_names = rows.find_all(class_="name")
    emoji_chars = rows.find_all(class_="chars")

    for code in emoji_codes:
        unicode = str(code.text)
        code_list = unicode.split(" ")
        emoji_code = "".join(list(map(combine_codes, code_list)))

        data["unicode"].append(emoji_code)

    for char in emoji_codes:
        data["chars"].append(char.text)

    for name in emoji_names:
        # convert names to strings, remove ⊛ symbols and reformat certain emojis (e.g. family and flags)
        emoji_name = str(name.text)

        if emoji_name[0] == "⊛":
            emoji_name = emoji_name[2:]

        data["fullname"].append(emoji_name.lower())


### Parsing
shortcodes_dict = {"unicode": [],
                    "shortcode": []}

for row in shortcodes_df.index:
    emoji = shortcodes_df.loc[row, "char"]
    unicode_string = emoji.encode('unicode-escape').decode('ASCII').upper()

    shortcodes_dict["unicode"].append(unicode_string)
    shortcodes_dict["shortcode"].append(row)

shortcode_lookup = pd.DataFrame(data=shortcodes_dict)

df = pd.DataFrame(data=data)


### Matching Shortcodes
combined_df = df.merge(shortcode_lookup, on="unicode", how="left")
combined_df["shortcode"].fillna(combined_df["fullname"], inplace=True)

convert_to_spaces(combined_df, True)


### Generate Yaml
generate_yaml(combined_df)