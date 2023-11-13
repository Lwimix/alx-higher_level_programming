#!/usr/bin/node
'use strict';
let i; let biggest = process.argv[2]; let secondBiggest;
secondBiggest = process.argv[3];
if (biggest === undefined || process.argv.length === 3) { console.log(0); } else {
  if (secondBiggest === undefined) { console.log(0); } else {
    for (i = 3; i < process.argv.length; i++) {
      if (biggest <= process.argv[i]) {
        secondBiggest = biggest;
        biggest = process.argv[i];
      } else {
        if (process.argv[i] > secondBiggest) { secondBiggest = process.argv[i]; }
      }
    }
    console.log(secondBiggest);
  }
}
