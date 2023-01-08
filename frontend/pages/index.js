import React, { useState, useEffect } from 'react'
import Spinner from '../components/spinner'
import Head from 'next/head'
import { useRouter } from 'next/router'

export default function Home() {

    const router = useRouter();

    const [loading, setLoading] = useState(true)

    useEffect(() => {
        sessionStorage.getItem('authenticated') === 'true' ? setLoading(false) : router.push('/login');
    }, [])

    return (
        <>
            <Head>
                <title>MyInstitute - Home</title>
            </Head>
            {
                loading ? <Spinner /> : <>
                    <div className='text-center text-red-600'>
                        Home Page of MyInstitute
                    </div>
                </>
            }
        </>
    )
}
