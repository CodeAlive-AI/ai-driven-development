"""Exercise screenshot capture without requiring a Windows desktop or UFO."""

import base64
import importlib.util
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch


class FakeMCP:
    def __init__(self, *args):
        pass

    def mount(self, server):
        pass

    def tool(self):
        return lambda function: function


def load_server():
    modules = {}
    for name in ("fastmcp", "pydantic", "ufo", "ufo.client", "ufo.client.mcp",
                 "ufo.client.mcp.mcp_registry", "ufo.client.mcp.local_servers"):
        modules[name] = types.ModuleType(name)
    modules["fastmcp"].FastMCP = FakeMCP
    modules["pydantic"].Field = lambda **kwargs: None
    modules["ufo.client.mcp.mcp_registry"].MCPRegistry = types.SimpleNamespace(
        is_registered=lambda name: True, get=lambda name: object()
    )
    modules["ufo.client.mcp.local_servers"].load_all_servers = lambda: None
    source = Path(__file__).resolve().parents[1] / "scripts" / "ufo_windows_qa_mcp_server.py"
    spec = importlib.util.spec_from_file_location("windows_qa_test_server", source)
    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, modules), patch.dict("os.environ", {"UFO_ROOT": ""}):
        spec.loader.exec_module(module)
    return module


class CaptureToFileTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = load_server()
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "screens" / "test.png"
        self.png = b"\x89PNG\r\n\x1a\nexample"

    async def test_writes_raw_and_data_url_results_without_returning_image(self):
        encoded = base64.b64encode(self.png).decode("ascii")
        for payload in (encoded, "data:image/png;base64," + encoded):
            raw = types.SimpleNamespace(structured_content={"result": payload})
            with patch.object(self.server, "_call_mounted_tool", AsyncMock(return_value=raw)):
                result = await self.server.qa_capture_to_file(str(self.path))
            self.assertEqual(result, {"ok": True, "path": str(self.path), "bytes": len(self.png)})
            self.assertEqual(self.path.read_bytes(), self.png)

    async def test_invalid_data_does_not_overwrite_existing_file(self):
        self.path.parent.mkdir()
        self.path.write_bytes(b"existing")
        for payload in ("invalid!", base64.b64encode(b"not a PNG").decode(), "data:image/jpeg;base64,AA=="):
            raw = types.SimpleNamespace(content=[types.SimpleNamespace(text=json.dumps(payload))])
            with patch.object(self.server, "_call_mounted_tool", AsyncMock(return_value=raw)):
                with self.assertRaises(ValueError):
                    await self.server.qa_capture_to_file(str(self.path))
            self.assertEqual(self.path.read_bytes(), b"existing")

    async def test_missing_data_and_invalid_paths_fail_explicitly(self):
        with patch.object(self.server, "_call_mounted_tool", AsyncMock(return_value={})) as call:
            for path in ("relative.png", str(self.path.with_suffix(".jpg"))):
                with self.assertRaises(ValueError):
                    await self.server.qa_capture_to_file(path)
            call.assert_not_awaited()
            result = await self.server.qa_capture_to_file(str(self.path))
        self.assertFalse(result["ok"])
        self.assertFalse(self.path.exists())


if __name__ == "__main__":
    unittest.main()
