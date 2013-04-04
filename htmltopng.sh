#!/usr/bin/bash
for f in out/*.html ; do
  n=$(basename $f .html)
  cat $f | sed -n -e 's/.*src=".*base64,\(.*\)" \/><br.*/\1/p' | base64 -d > png/$n.png
done
