const puppeteer = require('puppeteer');
const fs = require('fs');
const { createCanvas, loadImage } = require('canvas');

async function generateScreenshot() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`./src/index.html`);
    await page.setViewport({ width: 800, height: 480 });

    const screenshot = await page.screenshot({ type: 'png' });
    await browser.close();

    // Convert PNG to BMP using canvas
    const canvas = createCanvas(800, 480);
    const ctx = canvas.getContext('2d');
    const image = await loadImage(screenshot);
    ctx.drawImage(image, 0, 0);
    const buffer = canvas.toBuffer('image/bmp');
    fs.writeFileSync('page.bmp', buffer);
    console.log('Screenshot saved as page.bmp');
}

generateScreenshot();
