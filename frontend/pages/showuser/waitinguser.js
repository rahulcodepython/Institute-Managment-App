import React, { useState, useEffect } from 'react'
import { useRouter } from 'next/router'

export default function WaitingUser() {

    const router = useRouter();

    const [loading, setLoading] = useState(true)

    useEffect(() => {
        sessionStorage.getItem('position') === 'Admin' ? null : router.back()
    }, [])

    return (
        <div>Waiting User</div>
    )
}
