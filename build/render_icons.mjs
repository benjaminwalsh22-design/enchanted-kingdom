// Render the full-bleed (square-corner) icon base to assets/emblem_icon_1024.png.
// Derives emblem_icon.html from emblem.html by squaring the background corners.
// Usage (from build/):  node render_icons.mjs      (requires: npm install)
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';

const src = readFileSync('emblem.html', 'utf8')
  .replace('rx="230" fill="url(#bg)"', 'rx="0" fill="url(#bg)"');
writeFileSync('emblem_icon.html', src);

const browser = await chromium.launch();
const page = await (await browser.newContext({ viewport: { width: 1024, height: 1024 } })).newPage();
await page.goto('file://' + process.cwd() + '/emblem_icon.html');
await page.waitForTimeout(200);
await (await page.$('#wrap')).screenshot({ path: 'assets/emblem_icon_1024.png' });
await browser.close();
console.log('rendered assets/emblem_icon_1024.png');
