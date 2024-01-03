#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const json = JSON.parse(body);
  const charcts = json.results[1].characters;
  let i = 0;
  let name;
  while (i < charcts.length) {
    if (charcts[i].includes('18')) {
      name = charcts[i];
      break;
    }
    i++;
  }
  req(name, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const js = JSON.parse(body);
    console.log(js.films.length);
  });
});
