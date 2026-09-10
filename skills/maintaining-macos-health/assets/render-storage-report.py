#!/usr/bin/env python3
"""Attach scanner JSON to a cleanup plan or create a static inventory report.
No scanning, browser launch, HTTP server, or deletion is performed.
"""
import argparse
import importlib.util
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scan', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--plan', type=Path, help='Existing cleanup-plan JSON')
    args = parser.parse_args()
    scan = json.loads(args.scan.read_text())
    if 'stdout' in scan:
        scan = json.loads(scan['stdout'])
    if not all(k in scan for k in ('root', 'files', 'folders', 'errors')):
        raise ValueError('expected scanner JSON, not an arbitrary report')
    scan['coverage'] = ('Live scan; sizes include only accessible, non-excluded entries. '
                        + ('All discovered folders; ' if 'folder_tree' in scan else 'Top folders only; ')
                        + 'file list is top-K. Excluded directories: '
                        + ', '.join(scan.get('exclusions', [])))
    plan = json.loads(args.plan.read_text()) if args.plan else {'categories': []}
    plan['storage_scan'] = scan
    spec = importlib.util.spec_from_file_location('cleanup_renderer', Path(__file__).with_name('render-cleanup-plan.py'))
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    args.output.write_text(renderer.render_html(plan))


if __name__ == '__main__':
    main()
