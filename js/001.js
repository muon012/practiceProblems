// Function to make sure we don't display a question twice
function noDuplicates(arr) {
    var arrLen = arr.length;
    var arrCopy = arr.slice(); // Make copy of the array.
    for(var i = 0; i < arrLen; i++){

        // This random number will be used with the array copy.
        // The array copy will lose elements that's why we use the lenght of this copy and not the original's.
        var numberRandom = Math.floor(Math.random() * arrCopy.length);

        // We display a random element in the array copy:
        console.log(arrCopy[numberRandom]);

        // We then remove that element we randomly chose, so that the next random number will not be out of range.
        arrCopy.splice(numberRandom, 1);
    }
}

var abc = ['a', 'b', 'c', 'd', 'e'];


noDuplicates(abc);