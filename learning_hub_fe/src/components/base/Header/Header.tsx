import {Link} from "react-router-dom";
import './style.css'

export default function Header() {
    return <div className="header">
        <nav>
            <Link className="link" to='/'>Home</Link>
            <Link className="link" to="/courses">Courses</Link>
        </nav>
    </div>
}
