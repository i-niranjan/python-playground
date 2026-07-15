# Mini Project: Log Reader

Create a fake list of log lines.

Example:

```python
logs = [
    "INFO app started",
    "ERROR database failed",
    "INFO user logged in",
    "ERROR payment failed",
]
```

Build generators that:

- Yield one log line at a time
- Yield only error logs
- Yield only logs containing a search word

Then loop through the generators and print results.

