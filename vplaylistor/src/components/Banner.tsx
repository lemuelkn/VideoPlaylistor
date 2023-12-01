import React from 'react';
import './Banner.css'; // Import the CSS file for styling (you can customize styles here)

interface BannerProps {
  message: string;
  backgroundColor?: string;
  textColor?: string;
}

const Banner: React.FC<BannerProps> = ({
  message,
  backgroundColor = '#3498db',
  textColor = '#fff',
}) => {
  const bannerStyle = {
    backgroundColor,
    color: textColor,
  };

  return (
    <div className="banner" style={bannerStyle}>
      <p>Convert Spotify Music Playlist to Youtube Video playlist</p>
    </div>
  );
};

export default Banner;
