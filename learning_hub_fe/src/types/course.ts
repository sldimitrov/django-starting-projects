export interface Category {
    id: number;
    label: string;
}

export interface CourseEntity {
    id: number;
    title: string;
    description: string;
    category: Category;
    started_at: Date;
    finished_at: Date;
    slug: string;
}
