import json

def read_jsonl(path: str) -> list[dict]:
    result = []
    with open(str(path), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            mid = json.loads(line)
            result.append(mid)
    return result
    

def write_jsonl(rows: list[dict], path: str) -> None:
    with open(str(path), "w", encoding="utf-8") as f:
        for row in rows:
            line = json.dumps(row, ensure_ascii=False)
            f.write(line + "\n")