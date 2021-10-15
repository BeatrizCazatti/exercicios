var sel = document.getElementById('numeros')
var dados = document.getElementsByClassName('dados')
var lista = document.getElementsByTagName('li')
var numeros = []
var soma = 0
    

    sel.style.display='none'
    for( var x=0; x<=dados.length; x++){
        dados[x].style.listStyleType='none'
    }
    
    function adicionar(){
        //window.alert(numeros)
        var numtxt = document.getElementById('number')
        var num = Number(numtxt.value)
        sel.style.display='inline-block'
        
        if(numtxt.value.length == 0 ){ 
            window.alert('Digite o número a ser adicionado.')
        }else if(num < 1 || num > 100){
            window.alert('O número está fora do intervalo.')
            numtxt.value = ''
        }else if(numeros.indexOf(num) !== -1){
            window.alert('Esse número já foi adicionado.')
            numtxt.value = ''
        }else{
            numeros.push(Number(num))
            var item = document.createElement('option')
            item.text = num
            sel.appendChild(item)
            if(numeros.length > 10){
                sel.style.overflow=''
            }
        }
        numtxt.value = ''
        numtxt.focus()
    }

    function analisar(){
        numeros.sort();
        var maior = numeros[0]
        var menor = numeros[0]
        //n dá pra usar o sort() pq ele compara após transferir para string ai por exemplo na n sei o q Unicode o 100 < 2...
        for(var n=0;n<=numeros.length; n++){

            if(maior < numeros[n]){
                maior = numeros[n];
            }else if(menor > numeros[n]){
                menor = numeros[n]
            }
        }
        
        for(var c=0; c<numeros.length; c++){
            soma = soma + numeros[c]
        }

        function AproxOuN(){
            if(soma/numeros.length == Math.round(soma/numeros.length)){
                return ''
            }else{
                return ' aproximadamente'
            }
        }
        //console.log(`${n} é um número ${parouimp}.`)
        
        //soma = numeros[0] + numeros[1] + numeros[2] + numeros[3]
        lista[0].innerText = `Essa lista possue: ${Number(numeros.length)} números`;
        lista[1].innerText = `O menor número é: ${menor}`;
        lista[2].innerText = `O maior número é: ${maior}`;
        lista[3].innerText = `A soma de todos os números é: ${soma}`
        lista[4].innerText = `A média desses números é${AproxOuN()}: ${Math.round(soma/numeros.length)}`

        for( var x=0; x<=dados.length; x++){
            dados[x].style.listStyleType='square'
        }
    }