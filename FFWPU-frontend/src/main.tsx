import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Header from './Components/Header.tsx'
import MemberMenu from './Pages/MemberMenu.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Header />
    <MemberMenu />
  </StrictMode>,
)
