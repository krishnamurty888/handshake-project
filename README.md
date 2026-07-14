# Dynamo Log Report Fix

Fixed Terminal-Bench 2 (Harbor) task for parsing an Apache-style access log into a JSON summary report.

## Verification

Requires Docker and Harbor (`uv tool install harbor` or `pip install harbor`).

```bash
harbor run -p log-report -a oracle     # should PASS (reward 1)
harbor run -p log-report --agent nop     # should FAIL (reward 0)
```

## Fixes applied

1. **task.toml** — `artifacts` changed from wrong string to array `["/app/report.json"]`
2. **environment/Dockerfile** — pinned base image by digest; removed leaked `solution_hint.py`
3. **instruction.md** — added clear output path, JSON schema, and numbered success criteria
4. **tests/test_outputs.py** — validates actual report values, not just file existence
5. **tests/test.sh** — writes reward to `/logs/verifier/reward.txt` and generates `ctrf.json`
