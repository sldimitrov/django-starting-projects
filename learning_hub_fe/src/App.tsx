import './App.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./pages/Home/Home.tsx";
import Courses from "./pages/Courses/Courses.tsx";
import MainLayout from "./components/base/MainLayout/MainLayout.tsx";

function App() {

  return (
    <BrowserRouter>
      <Routes>
          <Route element={<MainLayout/>}>
              <Route path="/" element={<Home/>} />
              <Route path="/courses" element={<Courses/>} />
          </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
