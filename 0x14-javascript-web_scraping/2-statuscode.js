#!/usr/bin/node
const req = require('request');
req(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
