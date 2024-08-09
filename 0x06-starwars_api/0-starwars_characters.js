#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const mp = new Map();
let chrs = [];
const filmApiUrl = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/?format=json`;

request(filmApiUrl, (error, _, body) => {
  if (error) throw error;
  chrs = JSON.parse(body).characters;
  for (const character of chrs) {
    request(character.concat('?format=json'), (error, _, body) => {
      if (error) throw error;
      mp.set(character, JSON.parse(body).name);
      if (mp.size === chrs.length) for (const chr of chrs) console.log(mp.get(chr));
    });
  }
});
