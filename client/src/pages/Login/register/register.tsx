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

  const handleRegister = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (password !== confirmPassword) {
      alert('As senhas não coincidem.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:4000/api/user/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email: login, password }),
      });

      if (!response.ok) {
        throw new Error('Erro na solicitação de registro');
      }

      const data = await response.json();
      console.log('Usuário registrado:', data);

      // Redireciona para a tela de login após o registro bem-sucedido
      navigate('/login');
    } catch (error) {
      console.error('Erro:', error);
    }
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
        <div className='logo-ejov-notext'>
          <img src="src/assets/LogoEJOV-notext.png" alt="LogoEJOV" />
        </div>
        <h2>CADASTRAR CONTA</h2>
        <label htmlFor="name">NOME/SOBRENOME:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <label htmlFor="e-mail">E-MAIL:</label>
        <input
          type="text"
          id="login"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
        />
        <label htmlFor="password-rg">SENHA:</label>
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
        <label htmlFor="confirm-password-rg">CONFIRMAR SENHA:</label>
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
        <button type="submit" className="register-button">CADASTRAR</button>
      </form>
    </LayoutLogin>
  );
};

export default Register;
