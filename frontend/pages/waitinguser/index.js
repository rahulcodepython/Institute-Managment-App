import React, { useState, useEffect } from 'react'
import Spinner from '../../components/spinner';
import { useCookies } from 'react-cookie'
import { useRouter } from 'next/router';

export default function index() {

    const router = useRouter();

    const [loading, setLoading] = useState(true)
    const [approvalStatus, setApprovalStatus] = useState(0)

    const [cookies, setCookie, removeCookie] = useCookies(['userid', 'authenticated']);

    const checkWaitingUser = () => {
        const options = {
            method: 'GET'
        };

        const apiURL = `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/checkwaituser/${cookies.userid}`

        fetch(apiURL, options)
            .then(response => response.json())
            .then(response => {
                if (response.msg === 'Not Approved') {
                    setApprovalStatus(1)
                }

                else if (response.msg === "Rejected") {
                    removeCookie(['userid', 'authenticated'])
                    router.push('/register')
                }

                else {
                    console.log(response);
                }
            })
            .catch(err => console.error(err));
    }

    useEffect(() => {
        checkWaitingUser();
        setLoading(false)
    }, [])


    return (
        loading ? <Spinner /> : <div className='text-center my-5'>
            {
                approvalStatus === 1 ? 'Admin does not approved you till now, Please wait for the approval' : ''
            }
        </div>
    )
}
