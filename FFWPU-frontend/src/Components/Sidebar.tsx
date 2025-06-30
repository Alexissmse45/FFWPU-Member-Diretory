import React from 'react';
import '../assets/style/Sidebar.css';
import memberIcon from '../assets/Sidebar/member.png';
import dashboardIcon from '../assets/Sidebar/dashboard.png'; 

function Sidebar () {
  return (
    <div className="sidebar">
      <div className="sidebar-content">
        <ul className="nav-links">
          <li className="nav-item dashboard">
            <img src={dashboardIcon} alt="Dashboard" className="nav-icon dashboard-icon" />
            <span>Dashboard</span>
          </li>
          <li className="nav-item members">
            <img src={memberIcon} alt="Members" className="nav-icon member-icon" />
            <span>Members</span>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
