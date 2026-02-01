import {useNavigate, useParams} from "react-router-dom";
import './style.css'

export default function Course() {
    const { slug } = useParams()
    const navigate = useNavigate()

    // TODO: Fetch the course using the slug

    const goBack = () => {
        navigate(-1)
    }

    return <div>
        <header>
            <button onClick={goBack}>
                ← Back
            </button>
            <h1>Course</h1>
        </header>

        <section>
            {slug}
        </section>
    </div>
}
