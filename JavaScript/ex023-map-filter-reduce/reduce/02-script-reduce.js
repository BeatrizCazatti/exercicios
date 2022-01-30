const list = [
    {
        name: 'coffee',
        price: 20,
    },
    {
        name: 'coca-cola',
        price: 6,
    },
    {
        name: 'rice',
        price: 24,
    }
];

const balanceAvailable = 100;

function substract(balance, list){
    return list.reduce(function(prev, current, index){
        console.log("round", index +1)
        console.log({ prev })
        console.log({ current })
        return prev - current.price
    }, balanceAvailable);
}

console.log(substract(balanceAvailable, list));