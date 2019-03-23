'use strict';

const express = require('express');

// Constants
const PORT = 8200;
const HOST = "0.0.0.0";

// App
const app = express();
app.get('/', (req, res) => {
   var user_agent = req.headers['user-agent'];
   res.send("<h1>Hello from the simple Node.js Web app container</h1>" +
   		   "<p>I see your browser is: " + user_agent + "</p>" +
   		   "<h2>Thanks for visiting</h2>");
});

app.listen(PORT, HOST);
console.log("Running on http://${HOST}:${PORT}");


