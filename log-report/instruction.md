There is an Apache-style access log at `/app/access.log`. Parse it and write a
JSON summary report to `/app/report.json`.

The report must be a JSON object with these three keys:

- `total_requests` (integer): the total number of log lines in the file.
- `unique_ips` (integer): the number of distinct client IP addresses (the
  first whitespace-separated field of each log line).
- `top_path` (string): the request path (e.g. `/index.html`) that appears
  most often, parsed from the quoted request line (e.g.
  `"GET /index.html HTTP/1.1"`). If multiple paths are tied for the highest
  count, any one of them is acceptable.

## Success criteria

1. `/app/report.json` exists and contains a single valid JSON object.
2. The object has the keys `total_requests`, `unique_ips`, and `top_path`.
3. `total_requests` equals the number of non-empty lines in `/app/access.log`.
4. `unique_ips` equals the number of distinct IP addresses across those lines.
5. `top_path` equals the most-requested path in the log (or one of the tied
   top paths, if there is a tie).
