// src/pages/AssistanceScreens/components/nav-bar/nav-bar.tsx
import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './nav-bar.css';

const NavBar: React.FC = () => {
  const location = useLocation();
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <nav className="navbar">
      <Link to="/home" className="logo-placeholder desktop-only">
        <img src="src/assets/LogoEJOV-notext.png" alt="LogoNoText" />
      </Link>
      <button className="menu-button" onClick={toggleMenu}>
        &#9776; {/* Ícone de menu hamburguer */}
      </button>
      <div className={`nav-options ${menuOpen ? 'open' : ''}`}>
        {/* Inclui a logo dentro do menu no mobile */}
        <Link to="/home" className="logo-placeholder mobile-only">
          <img src="src/assets/LogoEJOV-notext.png" alt="LogoNoText" />
        </Link>
        <Link to="/assistance-form" className={`nav-item ${location.pathname === '/assistance-form' ? 'selected' : ''}`}>
          ASSISTÊNCIA
        </Link>
        <Link to="/status-list" className={`nav-item ${location.pathname === '/status-list' ? 'selected' : ''}`}>
          STATUS
        </Link>
        {/* Ícone do perfil também aparece dentro do menu no mobile */}
        <div className="profile-icon-placeholder mobile-only"></div>
      </div>
      <div className="profile-icon-placeholder desktop-only"></div> {/* Espaço reservado para o ícone do perfil no desktop */}
    </nav>
  );
};

export default NavBar;
