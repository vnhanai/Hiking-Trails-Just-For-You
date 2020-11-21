const fs = require('fs');
const path = require('path');
const neatCsv = require('neat-csv');

const filePath = path.join(__dirname, './us-zip-code-latitude-and-longitude.csv');

function searchZip(zipcode) {
  fs.readFile(filePath, async (error, data) => {
    if (error) {
      return console.log('error reading file');
    }
    const parsedData = await neatCsv(data);
    for(var i = 0; i < parsedData.length; i++) {
      if (parsedData[i][0] == zipcode) {
        console.log(parsedData[i][3], parsedData[i][4]);
        return parsedData[i][3], parsedData[i][4];
      }
    }
  });
};

module.exports.searchZip = searchZip;