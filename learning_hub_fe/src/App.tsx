import './App.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./pages/Home/Home.tsx";
import Courses from "./pages/Courses/Courses.tsx";
import MainLayout from "./components/base/MainLayout/MainLayout.tsx";
import Course from "./pages/Course/Course.tsx";

function App() {

  return (
    <BrowserRouter>
      <Routes>
          <Route element={<MainLayout/>}>
              <Route path="/" element={<Home/>} />
              <Route path="/courses">
                  <Route index element={<Courses/>} />
                  <Route path=":slug" element={<Course/>} />
              </Route>
          </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
