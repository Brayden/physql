const puppeteer = require('puppeteer');
const fs = require('fs');

async function generateScreenshot() {
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

    // Execute the command `python3 display_image.py`
    const { exec } = require('child_process');
    exec(`python3 display_image.py`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
    });
}

generateScreenshot();
