#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const json = JSON.parse(body);
  const items = json.results;
  let j = 0;
  let count = 0;
  while (j < items.length) {
    const charcts = json.results[j].characters;
    let i = 0;
    while (i < charcts.length) {
      if (charcts[i].includes('18')) {
        count++;
      }
      i++;
    }
    j++;
  }
  console.log(count);
});
