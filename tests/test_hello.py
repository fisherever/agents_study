import pytest
from agents_study.hello import main
    
def test_prints_name(capsys):
    code = main(["--name", "x"])
    assert code == 0
    out = capsys.readouterr().out
    assert "x" in out
    
def test_missing_name_exits_nonezero():
    with pytest.raises(SystemExit) as excinfo:
        main([])
    assert excinfo.value.code == 2