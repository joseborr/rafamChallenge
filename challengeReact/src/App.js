
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Configuracion from './components/Configuracion';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' />
        <Route path='/configuracion' component={Configuracion}/>
      </Routes>
    </Router>
  );
}

export default App;
