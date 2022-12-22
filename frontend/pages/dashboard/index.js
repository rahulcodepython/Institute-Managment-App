import React, { useState, useEffect } from 'react'
import Spinner from '../../components/spinner';
import Head from 'next/head';
import AdminLayout from '../../layout/adminLayout';

export default function Dashboard() {

    const [loading, setLoading] = useState(true)

    useEffect(() => {
        setTimeout(() => {
            setLoading(false)
        }, 1000);
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
                    dfskfjsdkfj
                </>
            }
        </AdminLayout>
    )
}
