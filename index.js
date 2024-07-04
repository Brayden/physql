const puppeteer = require('puppeteer');
const fs = require('fs');

async function generateScreenshot() {
    // const browser = await puppeteer.launch();
    // const browser = await puppeteer.launch({ executablePath: "chromium-browser" });
    // const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disabled-setupid-sandbox', '--disable-extensions'] });
    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
    });
    const page = await browser.newPage();
    await page.goto(`file://${__dirname}/src/index.html`);
    await page.setViewport({ width: 800, height: 480 });

    const screenshotPath = 'page.png';
    await page.screenshot({ path: screenshotPath, fullPage: true });
    await browser.close();

    console.log(`Screenshot saved as ${screenshotPath}`);
}

generateScreenshot();
