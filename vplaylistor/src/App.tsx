import React from 'react';
import Banner from './components/Banner/Banner';
import TextBox from './components/TextBox/TextBox'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Banner message='' backgroundColor='#3498db' textColor='#000'/>
      <TextBox/>
      </header>
    </div>
  );
}

export default App;
