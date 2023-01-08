import React, { useState, useEffect } from 'react'
import Spinner from '../../components/spinner';
import Head from 'next/head';
import AdminLayout from '../../layout/adminLayout';
import { useRouter } from 'next/router';

export default function Dashboard() {

    const router = useRouter();

    const [loading, setLoading] = useState(true)

    useEffect(() => {
        sessionStorage.getItem('authenticated') === 'true' ? setLoading(false) : router.push('/login');
    }, [])

    return (
        <AdminLayout>
            <Head>
                <title>
                    MyInstitute - Dashboard
                </title>
            </Head>
            {
                loading ? <Spinner /> : <>
                    Dashboard
                </>
            }
        </AdminLayout>
    )
}
