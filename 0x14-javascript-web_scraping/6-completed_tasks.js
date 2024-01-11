#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const str = '?userId=';
const dict = {};
req(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const json = JSON.parse(body);
  const uniqueid = new Set();
  json.forEach(it => {
    uniqueid.add(it.userId);
  });
  const len = uniqueid.size;
  for (const val of uniqueid.values()) {
    req(url + str + val, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const js = JSON.parse(body);
      let i = 0;
      const t = true;
      let comp = 0;
      while (i < js.length) {
        if (js[i].completed === t) {
          comp = comp + 1;
        }
        i++;
      }
      dict[val] = comp;
      if (Object.keys(dict).length === len) {
        console.log(dict);
      }
    });
  }
});
