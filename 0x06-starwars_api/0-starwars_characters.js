#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const filmurl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(filmurl, async (err, res, body) => {
  err && console.log(err);

  const charactersArray = (JSON.parse(res.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
