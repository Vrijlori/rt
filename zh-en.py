import json
import os

def merge_game_json():
    with open('zhCN1.json', 'r', encoding='utf-8') as f:
        zh_old = json.load(f).get("strings", {})

    with open('enGB.json', 'r', encoding='utf-8') as f:
        en_all = json.load(f).get("strings", {})

    with open('zhCN2.json', 'r', encoding='utf-8') as f:
        zh_new = json.load(f).get("strings", {})

    output_strings = {}
    added_count = 0

    for key, en_data in en_all.items():
        en_text = en_data.get("Text", "")
        offset = en_data.get("Offset", 0)

        if key in zh_old:
            output_strings[key] = zh_old[key]
        else:
            zh_text = zh_new.get(key, {}).get("Text", "")

            if zh_text:
                merged_text = f"{zh_text}({en_text})"
                added_count += 1
            else:
                merged_text = en_text

            output_strings[key] = {
                "Offset": offset,
                "Text": merged_text
            }

    final_json = {"strings": output_strings}
    with open('zhCN.json', 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)



if __name__ == "__main__":
    merge_game_json()