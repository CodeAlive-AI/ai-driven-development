// Minimal DOM contract test: expansion, pagination and text-only folder names.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
class Element {
  constructor(tag) { this.tag = tag; this.childNodes = []; this.events = {}; }
  append(...nodes) { this.childNodes.push(...nodes); }
  addEventListener(event, fn) { this.events[event] = fn; }
  set open(value) { this._open = value; if(this.events.toggle) this.events.toggle(); }
  get open() { return this._open; }
  querySelector(tag) {
    for (const node of this.childNodes) {
      if (node.tag === tag) return node;
      const found = node.querySelector?.(tag); if (found) return found;
    }
    return null;
  }
}
const rows = [[0, '/root', 0, 0, 0, 0]];
for(let i=1;i<=205;i++) rows.push([0, i===205?'<img src=x onerror=alert(1)>':`folder${i}`, 0, i, 0, 0]);
const data = {textContent:JSON.stringify({rows})};
const target = new Element('ul');
const document = {
  getElementById: id => id === 'folder-tree-data'?data:target,
  createElement: tag => new Element(tag),
  createTextNode: text => ({textContent:text})
};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../assets/storage-tree.js'),'utf8'),{document,Int32Array});
const list = target.querySelector('ul'), more = target.querySelector('button');
assert.equal(list.childNodes.length,100);
assert.equal(list.childNodes[0].querySelector('code').textContent,'<img src=x onerror=alert(1)>');
more.events.click(); assert.equal(list.childNodes.length,200);
more.events.click(); assert.equal(list.childNodes.length,205); assert.equal(more.hidden,true);
console.log('PASS lazy tree expansion, sorting, pagination, literal names');
