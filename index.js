const puppeteer = require('puppeteer');
const fs = require('fs');
const http = require('http');
const url = require('url');
const { exec } = require('child_process');

var index = 0;
var screenshotTimer;

async function generateScreenshot(instruction = null) {
    if (index === 2) {
        index = 0;
    } else {
        index++;
    }

    const response = await fetch(`https://app.outerbase.com/api/v1/ezql`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Source-Token': 'pi6l4umd9e7j763epktsj6runbvl2wef8x85sijctba9vfekndgcvdrhhkg1nr5g',
        },
        body: JSON.stringify({
            query: `${instruction}. Return the data with an 'x' and 'y' key value pair to render a bar chart.`,
            run: true,
        }),
    })

    let json = await response.json()
    let items = (await json.response?.results?.items) ?? []
    console.log('JSON Response: ', items)

    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
    });
    const page = await browser.newPage();
    const url = instruction ? `file://${__dirname}/src/index.html?index=${index}&instruction=${instruction}` : `file://${__dirname}/src/index.html?index=${index}`;
    await page.goto(url);
    await page.setViewport({ width: 800, height: 480 });

    // await 10 seconds for the page to load and query to load
    // await page.waitForTimeout(10000);

    // Javascript await for 5 seconds
    // await setTimeout(5000);
    await new Promise(resolve => setTimeout(resolve, 2000));

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
}

// Initialize the timer for the first time
resetTimer();

// Create an HTTP server
const server = http.createServer((req, res) => {
    // Parse the request URL
    const parsedUrl = url.parse(req.url, true);
    const { pathname, query } = parsedUrl;

    console.log('Receiving request: ', req.url, req.method);
    console.log('Parsed URL:', parsedUrl);
    console.log('Query parameters:', query);

    // Handle the /instruction endpoint
    if (pathname === '/instruction' && req.method === 'GET') {
        const instruction = query.instruction;
        console.log(`Received instruction: ${instruction}`);

        // Here you can make a network call or execute commands based on the instruction
        // For example:
        // if (instruction === 'update display') {
        //     generateScreenshot(instruction);
        // } else {
        //     console.log(`Unknown instruction: ${instruction}`);
        // }
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
