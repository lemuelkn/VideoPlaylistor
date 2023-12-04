import React, { useState } from 'react';
import App from '../../App';


interface SubmitButtonProps {
    spotifyLink: string
}


const SubmitButton: React.FC <SubmitButtonProps>= ({
    spotifyLink
}) => {
    const [isButtonDisabled, setIsButtonDisabled] = useState(false);

    //route API for onClick action to do the search action
    // use the 
    const onClick = () =>{
        setIsButtonDisabled((prevValue) => !prevValue);
    };

    return(<div>
        <button onClick={onClick} 
        disabled={isButtonDisabled}
        >
        {isButtonDisabled ? 'Button Disabled' : 'Button Enabled'}
        
        </button>
    </div>);
}

export default SubmitButton;