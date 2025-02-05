#!/bin/sh
curl "https://github.com/go-check/check" 2>/dev/null |grep "tag/v2" |sed -e 's,.*tag/v,,;s,\".*,,;' |head -n1

