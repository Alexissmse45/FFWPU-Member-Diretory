import React from 'react';
import Header from '../Components/Header';
import Sidebar from '../Components/Sidebar';

function MemberMenu() {
  return (
    <div>
      <Header />
      <Sidebar />
      <div
        className="main-content"
        style={{
          marginTop: '78px',      // below header
          marginLeft: '250px',    // pushed by sidebar
          padding: '1rem',
        }}
      >
        <p>Your main content goes here</p>
      </div>
    </div>
  );
}

export default MemberMenu;
