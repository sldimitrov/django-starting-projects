import {useEffect, useState} from "react";
import type {CourseEntity} from "../../types/course.ts";
import './style.css'
import {Link} from "react-router-dom";

export default function Courses() {
    const [courses, setCourses] = useState<CourseEntity[]>([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/courses/')
            .then(response => response.json())
            .then(data => setCourses(data))
            .catch(error => console.log(error));
    }, [])

    return <div className="courses-layout">
        <header>
            <h1>Courses Page</h1>
        </header>

        <section className="course-section">
            {courses.length >= 1 ? courses.map((course: CourseEntity, index) => (
                <div className="course-container" key={`${index}-course`}>
                    <header>
                        <h3>{course.title}</h3>
                        <span>{course.category.label}</span>
                    </header>
                    <section>
                        <p>{course.description}</p>
                        <Link to={`/courses/${course.slug}`} className="link">Enroll now</Link>
                    </section>
                </div>
            )) : <>
                No courses were found.
            </>}
        </section>
    </div>
}
