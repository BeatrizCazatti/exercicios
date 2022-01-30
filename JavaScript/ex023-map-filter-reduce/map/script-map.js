const apple = {
    value: 1,
}
const orange = {
    value: 2,
}

/*
 *
  com o parâmetro this:
 *
 * 
*/

/* function mapWithThis (arr, thisArg){
    return arr.map(function(item){
        return item * this.value
    }, thisArg)
}

const array = [2, 4]

console.log('this = apple =>', mapWithThis(array, apple))

console.log('this = orange =>', mapWithThis(array, orange)) */

/*
 *
  sem o parâmetro this:
 *
 * 
*/

function mapWithOutThis (arr){
    return arr.map(function (item){
        return item * item
    })
}

const array = [2, 4, 6, 8, 10]

console.log( mapWithOutThis(array))