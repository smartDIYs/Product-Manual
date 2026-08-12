# pdf_sections_to_pages_match_by_dotspace_free.py
# pip install pypdf  # なければ PyPDF2 で自動フォールバック

import re, json, unicodedata
from pathlib import Path

try:
    from pypdf import PdfReader  # type: ignore
except Exception:
    from PyPDF2 import PdfReader  # type: ignore

ROOT = Path(".")
PDF_PATH = ROOT / "README.pdf"
MD_PATH  = ROOT / "README.md"
OUT_JSON = ROOT / "page_numbers.json"

SKIP_PAGES = {2, 3}  # 1始まりで 2,3 ページを除外
RE_HEADING = re.compile(r'^\s*(\d+(?:[\.．]\d+){0,2})(?:[\.．])?\s+(.+?)\s*$')

EXTRA_TRANSLATE = str.maketrans({
    "⻑": "長",  # CJK Radical Long
    "⽂": "文",  # Kangxi radical (文)
})

# --- 比較用ノーマライズ ---
def normalize_for_match(s: str) -> str:
    # 1) NFKC（部首/互換形・全角英数記号・全角ドット/スペース等を正規化）
    s = unicodedata.normalize("NFKC", s)
    # 2) ゼロ幅・不可視系の除去（保険）
    s = s.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    # 3) ドットを全て除去（. と 全角．）
    s = s.replace(".", "").replace("．", "")
    # 4) すべての空白類（半角/全角/NBSP 等）を除去
    s = re.sub(r'[\s\u00A0\u2000-\u200D\u202F\u205F\u3000]+', "", s)
    # 互換文字を通常文字へ（全角英数/互換漢字/部首系なども寄ることがある）
    s = unicodedata.normalize("NFKC", s)
    # NFKCで取り切れないものがあれば追加置換（保険）
    s = s.translate(EXTRA_TRANSLATE)
    return s

# --- README.md の TOC からホワイトリスト（オリジナル→比較キー） ---
def build_allowed_map_from_readme(md_path: Path) -> dict[str, str]:
    """
    戻り値: { norm_key(ドット/スペース抜き・NFKC): original_title_from_TOC }
    """
    if not md_path.exists():
        return {}
    html = md_path.read_text(encoding="utf-8", errors="ignore")
    a_re    = re.compile(r'<a\s+class="[^"]*toc[^"]*"\s+href="[^"]*">([\s\S]*?)</a>', re.IGNORECASE)
    span_re = re.compile(r'<span[^>]*>([\s\S]*?)</span>', re.IGNORECASE)

    allowed_map: dict[str, str] = {}
    for a_html in a_re.findall(html):
        spans = span_re.findall(a_html)
        if not spans:
            continue
        original = re.sub(r'<[^>]+>', '', spans[0]).replace("&nbsp;", " ").strip()
        # 末尾のページ番号様ノイズを軽く掃除（" ... 12" など）
        original_clean_for_view = re.sub(r'\s+\d+\s*$', '', original)
        # 最大3階層の番号を持つもののみ採用（1 / 1.1 / 1.1.1）
        # 末尾ドットや直後の空白有無も大目に見る
        o_norm_for_check = unicodedata.normalize("NFKC", original_clean_for_view)
        if not re.match(r'^\d+(?:\.\d+){0,2}\.?\s*', o_norm_for_check):
            continue
        # 比較用ノーマライズキーを作成（ドット/空白を除去）
        norm_key = normalize_for_match(original_clean_for_view)
        # すでに同じキーがある場合は先勝ち（重複回避）
        allowed_map.setdefault(norm_key, original_clean_for_view)
    return allowed_map

# --- PDF から見出し抽出 → allowed_map で突合せしてページ付与 ---
def extract_sections(pdf_path: Path, allowed_map: dict[str, str]) -> dict[str, int]:
    reader = PdfReader(str(pdf_path))
    results: dict[str, int] = {}

    for page_index, page in enumerate(reader.pages, start=1):
        if page_index in SKIP_PAGES:
            continue
        text = page.extract_text() or ""
        if not text.strip():
            continue

        for raw in text.splitlines():
            line = raw.strip()
            m = RE_HEADING.match(line)
            if not m:
                continue
            num, title = m.groups()
            title = re.sub(r'\s+\d+\s*$', '', title)  # 行末のページ番号様ノイズ除去

            # PDF側の「表示文字列（オリジナルではない）」→ 比較用キー化
            pdf_key_display = f"{num.replace('．','.') } {title}"
            norm_pdf_key = normalize_for_match(pdf_key_display)

            if allowed_map:
                # ホワイトリスト比較（ドット/空白無視）
                if norm_pdf_key not in allowed_map:
                    continue
                # 出力キーは TOC オリジナル（ドット/スペースあり）
                out_key = allowed_map[norm_pdf_key]
            else:
                # README.md が無い場合は PDF表示文字列をそのままキーにする（従来モード）
                out_key = pdf_key_display

            results.setdefault(out_key, page_index)  # 1始まりページ番号
    return results

def main():
    allowed_map = build_allowed_map_from_readme(MD_PATH)
    mapping = extract_sections(PDF_PATH, allowed_map)
    OUT_JSON.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(mapping, ensure_ascii=False, indent=2))
    print(f"\nSaved: {OUT_JSON}")

if __name__ == "__main__":
    main()
