// Importing required modules
const http = require('http');

// Creating a server
const server = http.createServer((req, res) => {
  // Set the content type of the response
  res.setHeader('Content-Type', 'text/plain');

  // Sending "Hello, World!" as the response
  res.end('Hello, World!\n');
});

// Define the port to listen on
const port = process.env.PORT || 3000;

// Start the server and listen for incoming requests
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
