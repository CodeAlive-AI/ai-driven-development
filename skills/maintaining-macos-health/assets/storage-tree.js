(() => {
  const data = JSON.parse(document.getElementById('folder-tree-data').textContent);
  const tree = data.rows;
  const first = new Int32Array(tree.length).fill(-1);
  const next = new Int32Array(tree.length).fill(-1);
  for (let i = tree.length - 1; i > 0; i--) {
    next[i] = first[tree[i][0]];
    first[tree[i][0]] = i;
  }
  function size(value) {
    let unit = 0;
    const units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB'];
    while (value >= 1024 && unit < units.length - 1) { value /= 1024; unit++; }
    return value.toFixed(unit ? 2 : 0) + ' ' + units[unit];
  }
  function makeNode(id) {
    const row = tree[id];
    const li = document.createElement('li');
    const details = document.createElement('details');
    const summary = document.createElement('summary');
    const amount = document.createElement('span');
    amount.className = 'storage-size'; amount.textContent = size(row[3]);
    const name = document.createElement('code'); name.textContent = row[1];
    summary.append(amount, document.createTextNode(' '), name);
    if (row[4] || row[5]) {
      const status = document.createElement('span');
      status.textContent = ` — incomplete: ${row[4]} errors, ${row[5]} excluded`;
      summary.append(status);
    }
    if (first[id] === -1) {
      li.append(...summary.childNodes);
    } else {
      details.append(summary); li.append(details);
      let loaded = false;
      details.addEventListener('toggle', () => {
        if (!details.open || loaded) return;
        loaded = true;
        const ids = [];
        for (let i = first[id]; i !== -1; i = next[i]) ids.push(i);
        ids.sort((a, b) => tree[b][3] - tree[a][3] || tree[a][1].localeCompare(tree[b][1]));
        const ul = document.createElement('ul');
        const more = document.createElement('button'); more.type = 'button';
        let count = 0;
        const page = () => {
          const end = Math.min(count + 100, ids.length);
          while (count < end) ul.append(makeNode(ids[count++]));
          more.textContent = `Show more (${ids.length - count} remaining)`;
          more.hidden = count === ids.length;
        };
        more.addEventListener('click', page);
        details.append(ul, more); page();
      });
    }
    return li;
  }
  const target = document.getElementById('folder-tree');
  target.append(makeNode(0));
  const root = target.querySelector('details');
  if (root) root.open = true;
})();
