#!/usr/bin/node
const fs = require('fs');
const req = require('request');

req(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const respo = body;
  fs.writeFile(process.argv[3], respo, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
