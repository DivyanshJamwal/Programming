import { Route, Routes, useNavigate } from "react-router-dom"
import Navigation from "./components/Navigation"
import HelloWorldComponent from "./components/HelloWorld"
import GradeToggle from "./components/GradeToggle"
import StateManagement from "./components/StateManagement"
import Lpu from "./components/Lpu"
import Users from "./components/Users"
import Counter from "./components/Counter"
import Util from "./components/Util"
import Media from "./components/Media"
import PublicApiData from "./components/Api"
import TimerComp from "./components/Timer"
import Hoc from "./components/Hoc"
import LifecycleComponent from "./components/Lifecycle"
import ControlledForm from "./components/Form"
import Home from "./Home"
function App() {
  const navigate = useNavigate()
  const handleNavigate = () => {
    navigate('/')
  }
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/q1" element={<Navigation />} />
        <Route path="/q2" element={<Users />} />
        <Route path="/q3" element={<HelloWorldComponent />} />
        <Route path="/q5" element={<GradeToggle />} />
        <Route path="/q6" element={<StateManagement />} />
        <Route path="/q7" element={<Lpu />} />
        <Route path="/q8" element={<Counter />} />
        <Route path="/q9" element={<Util />} />
        <Route path="/q10" element={<Media />} />
        <Route path="/q11" element={<PublicApiData />} />
        <Route path="/q12" element={<TimerComp />} />
        <Route path="/q13" element={<ControlledForm />} />
        <Route path="/q14" element={<Hoc />} />
        <Route path="/q15" element={<LifecycleComponent />} />
      </Routes>
      <button onClick={handleNavigate}>Home</button>
    </>
  )
}

export default App
