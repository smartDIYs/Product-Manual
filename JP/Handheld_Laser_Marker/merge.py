# -*- coding: utf-8 -*-
import os.path
import json
import re
import subprocess
import os

CONTENT_DIR  = "./"
INDEXES_FILE = CONTENT_DIR + "__indexes.json"
OUTPUT_FILE  = CONTENT_DIR + "README.md"
NEWPAGE_CODE = '<div style="page-break-before:always"></div>'


## セクション番号を更新
def update_section_numbers(filepath, start_number=1):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.readlines()

    section_counter = start_number
    sub_section_counters = []

    def update_numbering(line):
        nonlocal section_counter
        nonlocal sub_section_counters

        # Match headers like "# 7. Title", "## 7.1 Subtitle", etc.
        match = re.match(r'^(#{1,3})\s+(\d+\.?(\d+\.?)*)?\s*(.*)', line)
        if match:
            hashes, _, _, title = match.groups()
            level = len(hashes)

            # Reset counters for deeper levels
            while len(sub_section_counters) < level - 1:
                sub_section_counters.append(0)
            while len(sub_section_counters) >= level:
                sub_section_counters.pop()

            # Increment counter for the current level
            if level == 1:
                sub_section_counters = []
                result = f"# {section_counter}. {title}"
                section_counter += 1
            else:
                if len(sub_section_counters) < level - 1:
                    sub_section_counters.append(1)
                else:
                    sub_section_counters[-1] += 1

                number = ".".join(map(str, [section_counter - 1] + sub_section_counters))
                result = f"{hashes} {number} {title}"

            return result + "\n"

        return line  # Return the line unchanged if it's not a header

    updated_content = [update_numbering(line) for line in content]

    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(updated_content)

def merge_sections(indexes_file, content_dir, output_file):

    f = open(indexes_file, 'r')
    json_array = json.load(f)
    f.close()

    document = ""

    for json_data in json_array:

        # Get File Path and Validate
        if "file" not in json_data:
            continue

        filepath = content_dir + json_data["file"]

        if os.path.exists(filepath) == False:
            print(filepath + " not found.")
            continue

        # Get Title
        title = json_data.get("title", "")

        # Conbine to document
        f = open(filepath)
        data = f.read()
        f.close()

        # # Add title
        # if title != "":
        #     document += "\n# " + title + "\n"

        document += data
        if json_data != json_array[-1]:
            document += "\n" + NEWPAGE_CODE + "\n\n"

    f = open(output_file, "w")
    f.write(document)
    f.close()

def update_section_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # ヘッダーと番号のマッピングを作成
    header_numbers = {}
    header_pattern = re.compile(r'^(#{1,3})\s+(\d+\.(\d+\.?)*)\s+(.*?)$', re.MULTILINE)

    for match in header_pattern.finditer(content):
        hashes, number, _, title = match.groups()
        # スペースを除去して正規化
        normalized_title = title.strip()
        header_numbers[normalized_title] = number#.rstrip('.')

    # リンクを更新
    def replace_link(match):
        link_text = match.group(1)
        link_target = match.group(2)

        # リンクテキストからヘッダー名を抽出 (既に番号が付いている場合は除去)
        text_header = re.sub(r'^\d+\.(\d+\.)?\s*', '', link_text)

        if text_header in header_numbers:
            number = header_numbers[text_header]
            # 特殊文字を除去するパターン
            clean_pattern = r'[^\w\s-]'
            # リンク先のアンカーを作成
            clean_header = re.sub(clean_pattern, '', text_header)
            anchor = f"{number.replace('.','')}-{clean_header.replace(' ', '_')}"
            # リンクテキストを更新
            new_text = f"{number} {text_header}"
            return f"[{new_text}](#{anchor})"

        return match.group(0)  # マッチするヘッダーがない場合は変更なし

    # マークダウンリンクのパターン
    link_pattern = r'\[(.*?)\]\(#(.*?)\)'
    updated_content = re.sub(link_pattern, replace_link, content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(updated_content)



def create_toc(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    with open("page_numbers.json", 'r', encoding='utf-8') as f:
        pages = json.load(f)

    # ヘッダーと番号で検索
    header_numbers = {}
    header_pattern = re.compile(r'^(#{1,3})\s+(\d+\.(\d+\.?)*)\s+(.*?)$', re.MULTILINE)
    html_lines = []

    for match in header_pattern.finditer(content):
        hashes, number, _, title = match.groups()
        normalized_title = title.strip()
        header_numbers[normalized_title] = number

        clean_pattern = r'[^\w\s-]'
        clean_header = re.sub(clean_pattern, '', normalized_title)
        anchor = f"{number.replace('.','')}-{clean_header.replace(' ', '_')}"
        new_text = f"{number} {normalized_title}"

        class_name = "toc-item"
        if hashes == "##":
            class_name = "toc-item toc-section-item"

        if hashes == "###":
            class_name = "toc-item toc-section-subitem"

        page_number = 0
        for section, page in pages.items():
            # print(f"{section} ... {new_text}")
            if section == new_text:
                page_number = page
        if page_number == 0:
            print(f"{new_text} page data not found.")

        code = []
        code.append(f'<a class="{class_name}" href="#{anchor}">')
        code.append(f'\t<span>{new_text}</span>')
        code.append(f'\t<span class="dots"></span>')
        code.append(f'\t<span class="page-number">{page_number}</span>')
        code.append(f'</a>')
        html_lines.extend(code)

    html_code = "\n".join(html_lines)

    updated_content = content.replace("<!-- custom toc -->", html_code)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(updated_content)


def main():

    # セクションをマージ
    merge_sections(INDEXES_FILE, CONTENT_DIR, OUTPUT_FILE)
    # セクション番号更新
    update_section_numbers(OUTPUT_FILE, start_number=1)
    # セクションリンク更新
    update_section_links(OUTPUT_FILE)

    create_toc(OUTPUT_FILE)


if __name__ == "__main__":
    main()
