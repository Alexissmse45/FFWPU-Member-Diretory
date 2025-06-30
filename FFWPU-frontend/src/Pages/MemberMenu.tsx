import React from 'react';
import Header from '../Components/Header';
import Sidebar from '../Components/Sidebar';
import { FaSyncAlt, FaPlus } from 'react-icons/fa';
import '../assets/style/MemberMenu.css';

function MemberMenu() {
  return (
    <div>
      <Header />
      <Sidebar />

      <div className="main-content">
        {/* Top bar */}
        <div className="top-bar">
          <h2 className="page-title">MEMBERS</h2>
          <button className="refresh-button">
            <FaSyncAlt className="refresh-icon" />
            Refresh
          </button>
        </div>

        {/* Filter + Search Row */}
        <div className="filter-bar">
          <input
            type="text"
            placeholder="Search members..."
            className="search-input"
          />

          <select className="filter-dropdown">
            <option>All Months</option>
            <option>January</option>
            <option>February</option>
            <option>March</option>
            {/* Add more months as needed */}
          </select>

          <select className="filter-dropdown">
            <option>All Region</option>
            <option>Luzon</option>
            <option>Visayas</option>
            <option>Mindanao</option>
          </select>

          <select className="filter-dropdown">
            <option>All Nations</option>
            <option>Philippines</option>
            <option>Japan</option>
            <option>Korea</option>
          </select>

          <button className="add-member-button">
            <FaPlus className="add-icon" />
            Add Members
          </button>
        </div>

        {/* Main content */}
        <p>Your main content goes here</p>
      </div>
    </div>
  );
}

export default MemberMenu;
