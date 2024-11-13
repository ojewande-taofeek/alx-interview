#!/usr/bin/node

const argv = process.argv;
const request = require('request');

try {
  request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}/`, (error, response, body) => {
    if (error) {
      console.log(`Error: ${error.message}`);
    } else if (response.statusCode === 200) {
      const film = JSON.parse(body);
      const charcaterUrl = film.characters;
      for (let i = 0; i < charcaterUrl.length; i++) {
        request(charcaterUrl[i], (error, response, body) => {
          if (error) {
            console.log(`Error: ${error.message}`);
          } else if (response.statusCode === 200) {
            const characterProfile = JSON.parse(body);
            console.log(characterProfile.name);
          } else {
            console.log(response.statusCode);
          }
        });
      }
    } else {
      console.log(response.statusCode);
    }
  }
  );
} catch (err) {
  console.log(err);
}
