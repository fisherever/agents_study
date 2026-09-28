from agents_study.jsonl import read_jsonl, write_jsonl
    
def test_empty_file_returns_empty_list(tmp_path):
    p = tmp_path / "empty.jsonl"
    p.touch()
    a = read_jsonl(str(p))
    assert a == []
    
def test_roundtrip(tmp_path):
    rows = [{"a": 1}, {"b": "中文"}]
    p = tmp_path / "data.jsonl"
    write_jsonl(rows, str(p))
    assert read_jsonl(str(p)) == rows
