const puppeteer = require('puppeteer');
const http = require('http');
const url = require('url');
const { exec } = require('child_process');
require('dotenv').config();

var index = 0;
var screenshotTimer;

async function generateScreenshot(instruction = null) {
    const apiKey = process.env.API_KEY;

    if (index === 2) {
        index = 0;
    } else {
        index++;
    }

    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
    });
    const page = await browser.newPage();
    const url = instruction ? `file://${__dirname}/src/index.html?instruction=${instruction}&apiKey=${apiKey}` : `file://${__dirname}/src/index.html?index=${index}&apiKey=${apiKey}`;
    await page.goto(url);
    await page.setViewport({ width: 800, height: 480 });

    // Javascript await for 3 seconds
    await new Promise(resolve => setTimeout(resolve, 3000));

    const screenshotPath = 'page.png';
    await page.screenshot({ path: screenshotPath, fullPage: true });
    await browser.close();

    console.log(`Screenshot saved as ${screenshotPath}`);

    // Execute the command `python3 display_image.py`
    exec(`python3 display_image.py`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return;
        }

        console.log('Updated the display...')
    });

    // Reset the timer
    resetTimer();
}

function resetTimer() {
    // Clear the existing timer
    if (screenshotTimer) {
        clearTimeout(screenshotTimer);
    }

    // Set a new timer
    // screenshotTimer = setTimeout(generateScreenshot, 60000);
    // Uncomment the line above to generate a screenshot every 60 seconds
}

// Initialize the timer for the first time
resetTimer();

// Create an HTTP server
const server = http.createServer(async (req, res) => {
    // Parse the request URL
    const parsedUrl = url.parse(req.url, true);
    const { pathname, query } = parsedUrl;

    console.log('Receiving request: ', req.url, req.method);
    // Handle the /instruction endpoint
    if (pathname === '/instruction' && req.method === 'GET') {
        const instruction = query.instruction;
        console.log(`Received instruction: ${instruction}`);

        // Generate a new screenshot with the instruction
        generateScreenshot(instruction ?? 'Default');

        // Send a response back to the client
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Instruction received');
    } else {
        // Handle 404 Not Found
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

// Start the server
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});
