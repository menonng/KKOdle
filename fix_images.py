import glob, json

for path in glob.glob("*.ipynb"):
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
    for cell in nb["cells"]:
        att = cell.pop("attachments", None)
        if att:
            src = "".join(cell["source"])
            for name, data in att.items():
                mime, b64 = next(iter(data.items()))
                src = src.replace("attachment:" + name, f"data:{mime};base64,{b64}")
            cell["source"] = src
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)