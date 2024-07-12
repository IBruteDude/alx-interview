#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
let chrs = [];
const mp = new Map();
request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}/?format=json`, (error, response, body) => {
  if (error) throw error;
  chrs = JSON.parse(body).characters;
  for (const character of chrs) {
    request(character.concat('?format=json'), (error, response, body) => {
      if (error) throw error;
      mp.set(character, JSON.parse(body).name);
      if (mp.size === chrs.length) for (const chr of chrs) console.log(mp.get(chr));
    });
  }
});
