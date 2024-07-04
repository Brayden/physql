const puppeteer = require('puppeteer');
const fs = require('fs');

async function generateScreenshot() {
    // const browser = await puppeteer.launch();
    const browser = await puppeteer.launch({ executablePath: "chromium-browser" });
    const page = await browser.newPage();
    await page.goto(`./src/index.html`);
    await page.setViewport({ width: 800, height: 480 });

    const screenshotPath = 'page.png';
    await page.screenshot({ path: screenshotPath, fullPage: true });
    await browser.close();

    console.log(`Screenshot saved as ${screenshotPath}`);
}

generateScreenshot();
