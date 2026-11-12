#!/usr/bin/env bash
set -euo pipefail
usage() { echo "Usage: $0 --issue-id ID --status STATUS [--comment FILE|--comment-text TEXT]"; exit 1; }
issue_id=; status=; comment_file=; comment_text=
while [[ $# -gt 0 ]]; do
  case $1 in
    --issue-id) issue_id=$2; shift 2;;
    --status) status=$2; shift 2;;
    --comment) comment_file=$2; shift 2;;
    --comment-text) comment_text=$2; shift 2;;
    *) usage;;
  esac
done
[[ -n $issue_id && -n $status ]] || usage
[[ -n $PAPERCLIP_API_KEY && -n $PAPERCLIP_API_URL ]] || { echo "Missing PAPERCLIP_API_KEY/URL"; exit 1; }
if [[ -n $comment_file ]]; then
  [[ -f $comment_file ]] || { echo "Comment file not found: $comment_file"; exit 1; }
  comment=$(cat "$comment_file")
else
  comment=$comment_text
fi
api_base="${PAPERCLIP_API_URL%/}"; api_base="${api_base%/api}"
payload=$(jq -n --arg status "$status" --arg comment "$comment" '{status: $status, comment: $comment}')
run_id=${PAPERCLIP_RUN_ID:-}
if [[ -z $run_id ]]; then
  echo "Missing PAPERCLIP_RUN_ID" >&2; exit 1
fi
echo "Calling: curl -X PATCH ... -H X-Paperclip-Run-Id: $run_id" >&2
curl -sS -X PATCH -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "X-Paperclip-Run-Id: $run_id" -H "Content-Type: application/json" \
  -d "$payload" "$api_base/api/issues/$issue_id" -w '\nHTTP:%{http_code}\n' --fail
if [[ $? -ne 0 ]]; then
  echo "ERROR: API call failed (non-zero exit or HTTP error)" >&2
  exit 1
fi
