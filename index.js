const puppeteer = require('puppeteer');
const fs = require('fs');
const http = require('http');
const url = require('url');
const { exec } = require('child_process');

var index = 0;
var screenshotTimer;

async function generateScreenshot() {
    if (index === 2) {
        index = 0;
    } else {
        index++;
    }

    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
    });
    const page = await browser.newPage();
    await page.goto(`file://${__dirname}/src/index.html?index=${index}`);
    await page.setViewport({ width: 800, height: 480 });

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
    screenshotTimer = setTimeout(generateScreenshot, 60000);
}

// Initialize the timer for the first time
resetTimer();

// Create an HTTP server
const server = http.createServer((req, res) => {
    // Parse the request URL
    const parsedUrl = url.parse(req.url, true);
    const { pathname, query } = parsedUrl;

    // Handle the /instruction endpoint
    if (pathname === '/instruction' && req.method === 'GET') {
        const instruction = query.instruction;
        console.log(`Received instruction: ${instruction}`);

        // Here you can make a network call or execute commands based on the instruction
        // For example:
        if (instruction === 'update display') {
            generateScreenshot();
        } else {
            console.log(`Unknown instruction: ${instruction}`);
        }

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


// const puppeteer = require('puppeteer');
// const fs = require('fs');

// var index = 0;

// async function generateScreenshot() {
//     if (index === 2) {
//         index = 0;
//     } else {
//         index++;
//     }

//     const browser = await puppeteer.launch({
//         executablePath: '/usr/bin/chromium-browser',
//     });
//     const page = await browser.newPage();
//     await page.goto(`file://${__dirname}/src/index.html?index=${index}`);
//     await page.setViewport({ width: 800, height: 480 });

//     const screenshotPath = 'page.png';
//     await page.screenshot({ path: screenshotPath, fullPage: true });
//     await browser.close();

//     console.log(`Screenshot saved as ${screenshotPath}`);

//     // Execute the command `python3 display_image.py`
//     const { exec } = require('child_process');
//     exec(`python3 display_image.py`, (error, stdout, stderr) => {
//         if (error) {
//             console.error(`exec error: ${error}`);
//             return;
//         }

//         console.log('Updated the display...')
//     });
// }

// generateScreenshot();

// // Call `generateScreenshot()` every 60 seconds
// setInterval(generateScreenshot, 60000);
