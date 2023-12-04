import React, {useState} from 'react';
import SubmitButton from '../SubmitButton/SubmitButton';
import './TextBox.css';

const TextBox: React.FC = () => {
    const [inputValue, setInputValue] = useState('');

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);

  };

  return(
    <div>
      <input
        type="text"
        id="textbox"
        value={inputValue}
        onChange={handleChange}
        placeholder="Enter spotify music playlist link"
        className='TextBox'
      />
      <SubmitButton spotifyLink= {inputValue}/>
    </div>

  );
}

export default TextBox;