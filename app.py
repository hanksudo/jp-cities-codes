import json
import pandas as pd
import nkf

src = "data/000618153.xls"

def to_hiragana(s):
    out = nkf.nkf("-w --hiragana", s)
    return out.decode("utf-8")

if __name__ == "__main__":
    save_names = (
        "prefectures",
        "cities"
    )
    replace_columns = (
        ("code", "prefecture", "city", "prefecture_kana", "city_kana"),
        ("code", "name", "hiragana")
    )
    idx = 0
    for sheet_name in pd.ExcelFile(src).sheet_names:
        print("Converting sheet name: {}".format(sheet_name))
        print()
        df = pd.read_excel(src, sheet_name=sheet_name, header=None if idx == 1 else 0, dtype=str)
        df.columns = replace_columns[idx]
        columns = list(df.columns)

        results = []
        for row in df.values:
            obj = dict(zip(columns, row))

            # R1.5.1現在の団体
            if idx == 0:
                if pd.isnull(obj["city_kana"]):
                    continue
                
                obj["prefecture_kana"] = to_hiragana(obj["prefecture_kana"])
                obj["city_kana"] = to_hiragana(obj["city_kana"])
                results.append(obj)
            # H30.10.1政令指定都市
            elif idx == 1:
                results.append(obj)
        
        with open("data/{}.json".format(save_names[idx]), "w") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        idx += 1
