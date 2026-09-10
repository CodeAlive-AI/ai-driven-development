import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'assets'))
from disk_safety import skill_audit
from disk_review import page

class BulkAudit(unittest.TestCase):
    def test_partial_scan_and_missing_binary_are_visible(self):
        with tempfile.TemporaryDirectory() as directory:
            home=Path(directory); (home/'Downloads').mkdir()
            scan={'root':str(home/'Downloads'),'allocated_bytes':1234,'errors':2,
                  'excluded_directories':1,'folders':[],'files':[]}
            def run(command, **kwargs):
                self.assertNotIn('/usr/bin/du', command)
                if '--json' in command:
                    return SimpleNamespace(returncode=2,stdout=json.dumps(scan),stderr='')
                return SimpleNamespace(returncode=0,stdout='',stderr='')
            with patch('disk_safety.subprocess.run',side_effect=run):
                rows,reports=skill_audit(home)
            self.assertEqual(rows[0]['size_bytes'],1234)
            self.assertFalse(rows[0]['selectable'])
            self.assertEqual(reports['storage_scan']['errors'],2)
            with patch('disk_safety.subprocess.run',side_effect=FileNotFoundError('scanner not built')):
                rows,reports=skill_audit(home)
            self.assertEqual(rows,[])
            self.assertEqual(len(reports['storage_scan']['failures']),1)
            document=page({'items':[],'reports':reports},'test-token')
            self.assertIn('scanner not built',document)
            self.assertIn('0 of 1 approved roots',document)

if __name__=='__main__': unittest.main()
