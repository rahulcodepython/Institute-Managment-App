import React, { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import Spinner from '../components/spinner'
import Sidebar from '../components/sidebar'

export default function Home() {

    const router = useRouter()

    const [loading, setLoading] = useState(true)
    const [authenticated, setAuthenticated] = useState(false)

    const checkUserIsAuthenticatedORNot = () => {
        sessionStorage.getItem("authenticated") === "true" ? setAuthenticated(true) : null
    }

    useEffect(() => {
        checkUserIsAuthenticatedORNot();

        sessionStorage.getItem("authenticated") === "true" ? null : router.push("/login");

        setLoading(false);
    }, [])

    return (
        <>
            {
                loading ? <Spinner /> : <>
                    {/* <div className='text-center text-red-600'>
                        Home Page
                    </div> */}
                    <Sidebar />
                </>
            }
        </>
    )
}
