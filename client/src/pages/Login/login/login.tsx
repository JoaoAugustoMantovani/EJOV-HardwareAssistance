import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FaEye, FaEyeSlash } from 'react-icons/fa';
import LayoutLogin from '../default-login-layout/layout-login';
import './login.css';

const Login: React.FC = () => {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const handleLogin = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('Login:', login, 'Password:', password);
    navigate('/dashboard');
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <LayoutLogin>
      <form className="login-form" onSubmit={handleLogin}>
        <div className='logo-ejov'>
          <img src="src/assets/LogoEJOV.png" alt="LogoEJOV" />
        </div>
        <label htmlFor="login">Login:</label>
        <input
          type="text"
          id="login"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
        />
        <label htmlFor="password">Senha:</label>
        <div style={{ display: 'flex', alignItems: 'center' }}>
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
            style={{ background: 'none', border: 'none', cursor: 'pointer' }}
            aria-label={showPassword ? 'Esconder senha' : 'Mostrar senha'}
          >
            {showPassword ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>
        <div className="login-links">
          <a href="/forgot-password">Esqueceu a senha?</a>
        </div>
        <button type="submit" className="login-button">Entrar</button>
        <p>
          Não possui uma conta? <a href="/register">Cadastrar conta</a>
        </p>
      </form>
    </LayoutLogin>
  );
};

export default Login;