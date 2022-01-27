class ContaBancaria {
    constructor(agencia, numero, tipo, saldo){
        this.agencia = agencia;
        this.numero = numero;
        this.tipo = tipo;
        this._saldo = 0;
    }

    sacar(value){
        if(value > this._saldo){
            return "Operação negada, saldo insuficiente."
        }

        this._saldo = this._saldo - value;

        return "Saldo disponível para saque: " + Math.round(this._saldo);
    }
    
    depositar(value){
        this._saldo = this._saldo + value;
    
        return "Saldo disponível para saque: " + Math.round(this._saldo);
    }
}
class ContaCorrente extends ContaBancaria {
    constructor(agencia, numero){
        super(agencia, numero);
        this.tipo = "corrente";
        this._cartaoCredito = cartaoCredito;
    }

    get cartaoCredito(){
        return this._cartaoCredito;
    }
    set cartaoCredito(value){
        this._cartaoCredito = value;
    }
}
class ContaPoupanca extends ContaBancaria {
    constructor(agencia, numero){
        super(agencia, numero);
        this.tipo = "poupança";
    }
}
class ContaUniversitaria extends ContaBancaria {
    constructor(agencia, numero){
        super(agencia, numero);
        this.tipo = "universitária";
    }

    sacar(value){
        if(value > 500){
            return "Operação negada, o valor limite é 500"
        }
        if(value > this._saldo){
            return "Operação negada, saldo insuficiente."
        }

        this._saldo = this._saldo - value;
    }
}

class ContaGoverno extends ContaBancaria {
    constructor(agencia, numero, nome, inflacao){
        super(agencia, numero, nome, inflacao);
        this.tipo = "governo"
        this.nome = nome
        this.inflacao = 0.05
    }
    
    sacar(value){
        if(value > 500){
            return "Operação negada, o valor limite é 500"
        }
        if(value > this._saldo){
            return "Operação negada, saldo insuficiente."
        }
        
        this._saldo = this._saldo - value;
        this._saldo = this._saldo - this._saldo * this.inflacao;

        return "Saldo disponível para saque: " + Math.round(this._saldo);
    }
    depositar(value){
        this._saldo = this._saldo + value;
        this._saldo = this._saldo - this._saldo * this.inflacao;
        
        return "Saldo disponível para saque: " + Math.round(this._saldo);
    }
}