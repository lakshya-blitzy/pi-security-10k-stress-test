def test_marker_exists():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    assert (root / "app" / "README_marker.txt").exists()
