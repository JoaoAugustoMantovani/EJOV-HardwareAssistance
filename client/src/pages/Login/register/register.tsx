import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FaEye, FaEyeSlash } from 'react-icons/fa';
import LayoutLogin from '../default-login-layout/layout-login';
import './register.css';

const Register: React.FC = () => {
  const [name, setName] = useState('');
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const navigate = useNavigate();

  const handleRegister = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (password !== confirmPassword) {
      alert('As senhas não coincidem.');
      return;
    }
    console.log('Nome:', name, 'Login:', login, 'Senha:', password);
    navigate('/dashboard');
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const toggleConfirmPasswordVisibility = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };

  return (
    <LayoutLogin>
      <form className="register-form" onSubmit={handleRegister}>
        <div className='logo-ejov'>
          <img src="src/assets/LogoEJOV.png" alt="LogoEJOV" />
        </div>
        <label htmlFor="name">Nome:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <label htmlFor="login">Login:</label>
        <input
          type="text"
          id="login"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
        />
        <label htmlFor="password">Senha:</label>
        <div className="password-input-container">
          <input
            type={showPassword ? 'text' : 'password'}
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ marginRight: '8px' }}
          />
          <button 
            type="button"
            onClick={togglePasswordVisibility}
            className="toggle-password-button"
            aria-label={showPassword ? 'Esconder senha' : 'Mostrar senha'}
          >
            {showPassword ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>
        <label htmlFor="confirm-password">Confirmar Senha:</label>
        <div className="password-input-container">
          <input
            type={showConfirmPassword ? 'text' : 'password'}
            id="confirm-password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            style={{ marginRight: '8px' }}
          />
          <button 
            type="button"
            onClick={toggleConfirmPasswordVisibility}
            className="toggle-password-button"
            aria-label={showConfirmPassword ? 'Esconder senha' : 'Mostrar senha'}
          >
            {showConfirmPassword ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>
        <button type="submit" className="register-button">Cadastrar</button>
        <p>
          Já possui uma conta? <a href="/login">Fazer login</a>
        </p>
      </form>
    </LayoutLogin>
  );
};

export default Register;