import importlib.util
from pathlib import Path
import unittest

source = Path(__file__).resolve().parents[1] / 'assets/render-cleanup-plan.py'
spec = importlib.util.spec_from_file_location('renderer', source)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class StorageReport(unittest.TestCase):
    def test_hierarchy_and_read_only_escaping(self):
        scan = {'folders': [
            {'path': '/data', 'allocated_bytes': 4096},
            {'path': '/data/missing/child', 'allocated_bytes': 1024},
            {'path': '/database', 'allocated_bytes': 2048}],
            'files': [{'path': '/data/<script>', 'allocated_bytes': 1},
                      {'path': '/data/big', 'allocated_bytes': 4096}]}
        document = renderer.render_storage_scan(scan)
        self.assertIn('<code>missing/child</code>', document)
        self.assertIn('<code>/database</code>', document)
        self.assertNotIn('<script>', document)
        self.assertIn('&lt;script&gt;', document)
        self.assertLess(document.index('/data/big'), document.index('&lt;script&gt;'))
        self.assertNotIn('<input', document)
        self.assertNotIn('item-cb', document)
        self.assertIn('Partial inventory', document)

    def test_compact_tree_escapes_script_and_rejects_invalid_parents(self):
        import json
        rows = [[0, "/data", 30, 20, 1, 0], [0, "</script><script>alert(1)", 10, 5, 0, 0]]
        # Folder names cannot contain slashes; test the script terminator at the root.
        rows[0][1] = "/data/</script>"
        rows[1][1] = "<img onerror=alert(1)>"
        output = renderer.render_compact_tree({'folder_tree_version': 1, 'folder_tree': rows})
        payload = output.split('id="folder-tree-data">', 1)[1].split('</script>', 1)[0]
        self.assertEqual(json.loads(payload)['rows'], rows)
        self.assertNotIn('<', payload)
        rows[1][0] = 1
        with self.assertRaises(ValueError):
            renderer.render_compact_tree({'folder_tree_version': 1, 'folder_tree': rows})

    def test_optional_unknown_and_validation(self):
        self.assertEqual(renderer.render_storage_scan(None), '')
        self.assertIn('Not measured', renderer.render_storage_scan({'files': [{'path': '/unknown'}]}))
        with self.assertRaises(ValueError):
            renderer.render_storage_scan({'files': [{'path': '/bad', 'allocated_bytes': -1}]})
        document = renderer.render_html({'categories': [], 'storage_scan': {'folders': [], 'files': []}})
        self.assertIn('No folder measurements', document)
        self.assertIn('No file measurements', document)


if __name__ == '__main__':
    unittest.main()
