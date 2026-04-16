
#!/usr/bin/env python3
import sys
import csv
import re
from bs4 import BeautifulSoup

time_re = re.compile(r'\d+:\d{2}(?:\.\d+)?|\d+\.\d+')

def text_of(node):
    return ' '.join(node.get_text(separator=' ', strip=True).split())

def find_deepest_table(td):
    tables = td.find_all('table')
    return tables[-1] if tables else None

def parse_row(tr):
    tds = tr.find_all('td')
    if not tds:
        return None
    texts = [text_of(td) for td in tds]
    ctypes = [td.get('data-celltype','').lower() for td in tds]

    rank = ''
    name = ''
    school = ''
    time = ''

    # prefer explicit data-celltype attributes
    for txt, ct in zip(texts, ctypes):
        if ct == 'rank' and not rank:
            rank = txt
        elif ct in ('name', 'athlete') and not name:
            name = txt
        elif ct in ('school','team') and not school:
            school = txt
        elif ct == 'time' and not time:
            time = txt

    # fallback: detect time-like text anywhere
    if not time:
        for txt in texts[::-1]:
            m = time_re.search(txt)
            if m:
                time = m.group(0)
                break

    # fallback rank detection: first numeric token
    if not rank:
        for txt in texts:
            token = txt.strip()
            if token.isdigit():
                rank = token
                break

    # fallback name: assume common order rank, name, school, time
    if not name:
        if len(texts) >= 2 and not time_re.search(texts[1]) and not texts[1].strip().isdigit():
            name = texts[1]
        else:
            for txt in texts:
                if txt and not time_re.search(txt) and not txt.strip().isdigit():
                    name = txt
                    break

    # fallback school: often the next cell after name
    if not school:
        # try index-based heuristic
        if len(texts) >= 3 and texts[2] != name and not time_re.search(texts[2]):
            school = texts[2]
        else:
            for txt in texts:
                if txt and txt != name and not time_re.search(txt) and not txt.strip().isdigit():
                    school = txt
                    break

    # final normalization
    rank = rank.strip()
    name = name.strip()
    school = school.strip()
    time = time.strip()
    if not (rank or name or school or time):
        return None
    return {'rank': rank, 'name': name, 'school': school, 'time': time}

def extract_event_rows(event_th):
    rows = []
    event_tr = event_th.find_parent('tr')
    # next tr should be region headers (West / East)
    region_header_tr = event_tr.find_next_sibling('tr')
    if not region_header_tr:
        return rows
    regions = [text_of(th) for th in region_header_tr.find_all('th')]
    data_tr = region_header_tr.find_next_sibling('tr')
    if not data_tr:
        return rows
    tds = data_tr.find_all('td')
    for idx, td in enumerate(tds):
        region = regions[idx] if idx < len(regions) else ''
        inner = find_deepest_table(td) or td
        for tr in inner.find_all('tr'):
            parsed = parse_row(tr)
            if parsed:
                rows.append({
                    'event': text_of(event_th),
                    'region': region,
                    'rank': parsed.get('rank',''),
                    'name': parsed.get('name',''),
                    'school': parsed.get('school',''),
                    'time': parsed.get('time','')
                })
    return rows

def main(inp_path, out_path):
    with open(inp_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    out_rows = []
    # event headers appear as th colspan=2; iterate them in document order
    for th in soup.find_all('th', attrs={'colspan': True}):
        # ignore small headers like the West/East row (they don't have colspan=2 as event rows do)
        try:
            if int(th.get('colspan')) != 2:
                continue
        except:
            continue
        title = text_of(th)
        if not title:
            continue
        rows = extract_event_rows(th)
        out_rows.extend(rows)

    # write CSV
    with open(out_path, 'w', newline='', encoding='utf-8') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=['event','region','rank','name','school','time'])
        writer.writeheader()
        for row in out_rows:
            writer.writerow({
                'event': row.get('event',''),
                'region': row.get('region',''),
                'rank': row.get('rank',''),
                'name': row.get('name',''),
                'school': row.get('school',''),
                'time': row.get('time','')
            })

    print(f"Wrote {len(out_rows)} rows to {out_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python refactor.py input.html output.csv")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
