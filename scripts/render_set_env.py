#!/usr/bin/env python3
import json
import os
import sys
import urllib.parse
import urllib.request

API_BASE = "https://api.render.com/v1"


def load_env_file(path):
    env = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            if "=" not in raw:
                continue
            key, value = raw.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key:
                env[key] = value
    return env


def request(method, url, token, data=None):
    payload = None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if data is not None:
        payload = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=payload, method=method, headers=headers)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode("utf-8")
        return json.loads(body) if body else None


def fetch_existing_env_vars(service_id, token):
    items = []
    cursor = None
    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor
        url = f"{API_BASE}/services/{service_id}/env-vars?{urllib.parse.urlencode(params)}"
        batch = request("GET", url, token) or []
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        cursor = batch[-1].get("cursor")
        if not cursor:
            break
    env_map = {}
    for item in items:
        env = item.get("envVar") or {}
        key = env.get("key")
        if key is not None:
            env_map[key] = env.get("value", "")
    return env_map


def main():
    token = os.getenv("RENDER_API_KEY")
    service_id = os.getenv("RENDER_SERVICE_ID")
    env_file = sys.argv[1] if len(sys.argv) > 1 else ".render.env"

    if not token or not service_id:
        print("Missing RENDER_API_KEY or RENDER_SERVICE_ID.")
        sys.exit(1)

    if not os.path.exists(env_file):
        print(f"Env file not found: {env_file}")
        sys.exit(1)

    new_env = load_env_file(env_file)
    if not new_env:
        print("No variables found in env file.")
        sys.exit(1)

    existing = fetch_existing_env_vars(service_id, token)
    merged = {**existing, **new_env}
    payload = [{"key": k, "value": v} for k, v in merged.items()]

    url = f"{API_BASE}/services/{service_id}/env-vars"
    request("PUT", url, token, data=payload)

    print("Environment variables updated.")


if __name__ == "__main__":
    main()
