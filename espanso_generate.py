# %%
import pandas as pd
from pathlib import Path

DIR = "emojis.csv"
OUTPUT_DIR = str(Path.cwd()) + "/espanso_package/package.yml"


df = pd.read_csv(DIR)
df.head()

# define yml elements
matches = "matches:\n"
trigger = "  - trigger: "
replace = "\n    replace: "

body = ""

# iterate through df and add to output string
for index, row in df.iterrows():
    name = row["name"]
    code = row["code"]

    name = "\":" + name + ":\""
    code = "\"" + code + "\""

    emoji_item = trigger + name + replace + code + "\n"
    body = body + emoji_item

yml_output = matches + body

# save to yml file
with open(OUTPUT_DIR, "w") as f:
    f.write(yml_output)
