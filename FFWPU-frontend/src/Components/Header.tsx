import React from 'react';
import '../assets/style/Header.css';
import logo from '../assets/logo.png';
import bellIcon from '../assets/Headbar/Bell.png';
import calendarIcon from '../assets/Headbar/Calendar.png';
import chatIcon from '../assets/Headbar/Chat.png';
// import userImage from '../assets/logo.png'; // Replace with your user image path

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        {/* Left side */}
        <div className="left-section">
          <img src={logo} alt="Logo" className="logo" />
          <div className="header-names">
            <h1 className="main-name">
              FAMILY FEDERATION FOR <br />
              WORLD PEACE AND <br />
              UNIFICATION
            </h1>
          </div>
        </div>

       <div className="right-section">
        <img src={calendarIcon} alt="Calendar" className="header-icon" />
        <img src={chatIcon} alt="Chat" className="header-icon" />
        <img src={bellIcon} alt="Bell" className="header-icon" />

        {/* Username container */}
        <div className="username">
          <img src={logo} alt="User" className="user-image-inside" />
          <span>JohnRegory</span>
        </div>
      </div>
      </div>
    </header>
  );
}

export default Header;
