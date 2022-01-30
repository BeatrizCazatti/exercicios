function addNumbers(arr){
    return array.reduce(function (prev, current){
        console.log({prev})
        console.log({current})
        
        return prev + current
    })
}

const array = [1, 2, 4]

console.log(addNumbers(array))