// Render the emblem SVG (emblem.html) to a 1024×1024 PNG using headless Chromium.
// Usage (from build/):  node render_emblem.mjs      (requires: npm install)
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await (await browser.newContext({ viewport: { width: 1024, height: 1024 } })).newPage();
await page.goto('file://' + process.cwd() + '/emblem.html');
await page.waitForTimeout(200);
await (await page.$('#wrap')).screenshot({ path: 'assets/emblem_1024.png' });
await browser.close();
console.log('rendered assets/emblem_1024.png');
