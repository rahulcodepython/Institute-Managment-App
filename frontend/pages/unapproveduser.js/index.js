import React, { useEffect, useState } from 'react'
import { useRouter } from 'next/router'
import Head from 'next/head'
import Spinner from '../../components/spinner';

export default function UnregisterUser() {

    const router = useRouter();

    const [loading, setLoading] = useState(true)

    useEffect(() => {
        sessionStorage.getItem('authenticated') === 'pending' ? setLoading(false) : router.push('/');
    }, [])

    return (
        <>
            <Head>
                <title>MyInstitute - Unapproved User</title>
            </Head>
            {
                loading ? <Spinner /> : 'You are unapproved'
            }
        </>
    )
}
