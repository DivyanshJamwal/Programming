import logo from './logo.svg';
import './App.css';
import LandingScreen from './screens/LandingScreen';
import Sb_parent from './components/LandingScreen/Practice/Sb_parent';
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Cards from './components/LandingScreen/Practice/Cards';
import Reservation from './screens/Reservation';
import Navbar from './components/LandingScreen/Navbar';
function App() {
  return (
    <>
    <BrowserRouter>
    {/* <Sb_parent /> */}
    {/* <Cards /> */}
    <Navbar/>
      <Routes>
        <Route path='/' element={<LandingScreen/>} ></Route>
        <Route path='/reservation' element={<Reservation/>} ></Route>
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
