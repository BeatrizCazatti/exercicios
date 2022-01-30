
function isItPair (arr){
    return arr.filter(function(item) {
        return item % 2 == 0
    })
}

const numbers = [1, 2, 3, 4, 6, 7, 8]

console.log(isItPair(numbers))