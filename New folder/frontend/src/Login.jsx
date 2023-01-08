import React from 'react'
// import { useSearchParams } from "react-router-dom";
import { useParams } from 'react-router-dom'

export default function Login() {

    // const [searchParams] = useSearchParams();
    const { id } = useParams()

    console.log(id);

    return (
        <div>login</div>
    )
}
