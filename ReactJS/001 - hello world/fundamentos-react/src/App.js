import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//
//hello world
/*/
function soma(a, b) {
  return a + b;
};

function primeiroJSX() {
  return (
    <div>
      Beatriz Cazatti
    </div>
  );
};

const App = () => {
  return (
    <div className='App verde'>
        {primeiroJSX()}
        {soma(10, 20)}
    </div>
  );
};

export default App;
const rootElement = document.getElementById('root')
ReactDOM.render(<App />, rootElement)

/*/
//aula 02 - renderização
//
const element = "Aqui é Beatriz"
const element2 = <div>React</div>

const App = () => {
  return (
    <div className='App'>
      {element}
      {element2}
    </div>
  )
}
export default App;
const rootElement = document.getElementById('root')
ReactDOM.render(<App />, rootElement)



