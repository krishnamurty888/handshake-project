import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth computed by hand from environment/access.log (6 lines):
# 192.168.0.1 GET /index.html, 192.168.0.2 GET /about.html, 192.168.0.1 GET /index.html,
# 10.0.0.5 POST /api/login, 192.168.0.2 GET /index.html, 10.0.0.5 GET /about.html
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH_CANDIDATES = {"/index.html"}  # count 3, vs /about.html=2, /api/login=1


def test_criterion_1_report_exists_and_is_valid_json():
    """instruction.md success criterion 1: /app/report.json exists and contains
    a single valid JSON object."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    data = json.loads(REPORT_PATH.read_text())
    assert isinstance(data, dict), "report.json must contain a single JSON object"


def test_criterion_2_report_has_required_keys():
    """instruction.md success criterion 2: the object has the keys
    total_requests, unique_ips, and top_path."""
    data = json.loads(REPORT_PATH.read_text())
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in data, f"report.json is missing required key {key!r}"


def test_criterion_3_total_requests_correct():
    """instruction.md success criterion 3: total_requests equals the number
    of non-empty lines in /app/access.log."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["total_requests"] == EXPECTED_TOTAL_REQUESTS, (
        f"total_requests: expected {EXPECTED_TOTAL_REQUESTS}, got {data['total_requests']!r}"
    )


def test_criterion_4_unique_ips_correct():
    """instruction.md success criterion 4: unique_ips equals the number of
    distinct IP addresses across those lines."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"unique_ips: expected {EXPECTED_UNIQUE_IPS}, got {data['unique_ips']!r}"
    )


def test_criterion_5_top_path_correct():
    """instruction.md success criterion 5: top_path equals the most-requested
    path in the log (or one of the tied top paths, if there is a tie)."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["top_path"] in EXPECTED_TOP_PATH_CANDIDATES, (
        f"top_path: expected one of {sorted(EXPECTED_TOP_PATH_CANDIDATES)}, got {data['top_path']!r}"
    )
