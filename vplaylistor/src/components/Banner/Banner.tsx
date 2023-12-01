import React from 'react';
import './Banner.css'; // Import the CSS file for styling (you can customize styles here)

interface BannerProps {
  message: string;
  backgroundColor: string;
  textColor: string;

}

const Banner: React.FC<BannerProps> = ({
  message,
  backgroundColor = '#3498db',
  textColor = '#fff',
}) => {
  const bannerStyle = {
    backgroundColor,
    color: textColor,
    boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)', 
  };

  return (
    <div className="banner" style={bannerStyle}>
      <p>Spotify Music playlist to Youtube Video Playlist</p>
    </div>
  );
};

export default Banner;
