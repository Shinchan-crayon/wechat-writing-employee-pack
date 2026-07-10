#!/usr/bin/env python3
"""Check the current public outbound IP for platform allowlist setup."""

from __future__ import annotations

import sys
import urllib.error
import urllib.request


SERVICES = (
    "https://api.ipify.org",
    "https://ifconfig.me/ip",
    "https://icanhazip.com",
)


def main() -> int:
    errors: list[str] = []
    for url in SERVICES:
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "wechat-writing-employee-pack-ip-check/1.0"},
            )
            with urllib.request.urlopen(request, timeout=8) as response:
                ip = response.read().decode("utf-8", errors="replace").strip()
            if ip:
                print(ip)
                return 0
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f"{url}: {exc}")

    print("无法自动查询公网出口 IP。请手动打开 IP 查询网站后填写到 USER.md。", file=sys.stderr)
    for item in errors:
        print(f"- {item}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
