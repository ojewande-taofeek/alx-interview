#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const { promisify } = require('util');
const requestPromise = promisify(request);

async function starsWarsCharcaters () {
  try {
    const response = await requestPromise(`https://swapi-api.alx-tools.com/api/films/${argv[2]}/`);
    if (response.statusCode === 200) {
      const episode = JSON.parse(response.body);
      const characterUrls = episode.characters;

      for (const characterUrl of characterUrls) {
        const characterProfileResponse = await requestPromise(characterUrl);
        if (characterProfileResponse.statusCode === 200) {
          const characterProfile = JSON.parse(characterProfileResponse.body);
          console.log(characterProfile.name);
        } else {
          console.log(`Character Error: ${characterProfileResponse.statusCode}`);
        }
      }
    } else {
      console.log(`Error: ${response.statusCode}`);
    }
  } catch (error) {
    console.log(`Error ${error.message}`);
  }
}

starsWarsCharcaters();
