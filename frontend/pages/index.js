import React, { useState, useEffect } from 'react'
import Spinner from '../components/spinner'
import Head from 'next/head'

export default function Home() {

    const [loading, setLoading] = useState(true)

    useEffect(() => {
        setTimeout(() => {
            setLoading(false);
        }, 2000);
    }, [])

    return (
        <>
            <Head>
                <title>MyInstitute - Home</title>
            </Head>
            {
                loading ? <Spinner /> : <>
                    <div className='text-center text-red-600'>
                        Home Page
                    </div>
                </>
            }
        </>
    )
}
