"""Codex session recovery script - restores missing threads from JSONL rollout files.
This was executed during the 2026-07-20 recovery session.
Reference only - paths and environment are specific to that session.
"""

import sqlite3, os, re, json, datetime, shutil

def extract_meta(fpath):
    """Extract session_id, cwd, timestamp, and first user message from a JSONL file."""
    with open(fpath, 'r', encoding='utf-8') as f:
        first = json.loads(f.readline())
        if first.get('type') != 'session_meta':
            return None
        p = first.get('payload', {})
        sid = p.get('session_id', '')
        cwd = p.get('cwd', '')
        title = ''; preview = ''
        for line in f:
            d = json.loads(line)
            if d.get('type') == 'event_msg' and d.get('payload', {}).get('type') == 'user_message':
                msg = d['payload'].get('message', '')
                if msg and isinstance(msg, str):
                    title = msg.strip().split(chr(10))[0][:100]
                    preview = msg.strip()[:200]
                break
        ts = 0
        ts_str = p.get('timestamp', '')
        if ts_str:
            ts = int(datetime.datetime.fromisoformat(ts_str.replace('Z', '+00:00')).timestamp())
        return {'id': sid, 'rollout_path': fpath, 'cwd': cwd, 'title': title, 'first_user_message': preview, 'preview': preview, 'created_at': ts, 'updated_at': ts}