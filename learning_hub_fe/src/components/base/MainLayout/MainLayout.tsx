import Footer from "../Footer/Footer.tsx";
import Header from "../Header/Header.tsx";
import {Outlet} from "react-router-dom";
import './style.css'

export default function MainLayout() {
    return (
        <div className="app-container">
            <Header/>
            <main className="main-layout">
                <Outlet/>
            </main>
            <Footer/>
        </div>
    )
}
