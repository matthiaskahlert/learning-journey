const books = `[{"author": "austen","firstname": "Jane","books": [{"title": "Mansfield Park", "published": 1814},{"title": "Stolz und Vorurteil", "published": 1813},{"title": "Emma", "published": 1816}]}, {"author": "Pratchett","firstname": "Terry","books": [{"title": "Total verhext", "published": 1991},{"title": "Lords and Ladys", "published": 1992},{"title": "Ruhig Blut", "published": 1996}]}]`;
const booksParsed = JSON.parse(books);
console.log(booksParsed);

console.log(booksParsed[1].author);
console.log(`${booksParsed[1].firstname} ${booksParsed[1].author}`);

const color = {
number : 120, Tightness : 73, saturation : 75, name : "lightgreen"
1
description: "Helles Grün"
kombi : function (elem) {
elem.style - "background: hsl(${this.number},
${this.saturation}%, ${this. lightness}%)';
const myObjectString = JSON.stringify(color);
console. log("myObjectString", myObjectString);
console. log(encodeURIComponent(myObjectString));