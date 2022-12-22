import React, { useState, useEffect } from 'react'
import AdminLayout from '../../layout/adminLayout'
import Spinner from '../../components/spinner'
import Head from 'next/head';

export default function ProfileCard() {

    const [profile, setProfile] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const options = {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${sessionStorage.getItem("accessToken")}`
            }
        };

        const apiURL = `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/myprofile/`

        fetch(apiURL, options)
            .then(response => response.json())
            .then(response => {
                setProfile(
                    sessionStorage.getItem('position') === 'Staff' || sessionStorage.getItem('position') === 'Admin' ? [
                        response[0].staffImage,
                        [
                            ['Joining Date', response[0].staffJoiningDate],
                            ['Gender', response[0].staffGender],
                            ['Mobile No', response[0].staffMobileNumber],
                            ['Pay Scale', response[0].staffPayScale],
                        ],
                        response[0].staffName,
                        response[0].staffUser,
                        ['POSITION', response[0].staffDepartment],
                        response[0].staffBio,
                    ]
                        :
                        sessionStorage.getItem('position') === 'Student' ? [
                            response[0].studentImage,
                            [
                                ['Joining Date', response[0].studentJoiningDate],
                                ['Gender', response[0].studentGender],
                                ['Mobile No', response[0].studentMobileNumber],
                                ['Class', response[0].studentClass],
                                ['Marks', response[0].studentMarks],
                                ['Ratings', response[0].studentRating],
                            ],
                            response[0].studentName,
                            response[0].studentUser,
                            ['SUBJECT', response[0].studentSubject],
                            response[0].studentBio,
                            response[0].studentRemarks,
                        ]
                            :
                            sessionStorage.getItem('position') === 'Teacher' ? [
                                response[0].teacherImage,
                                [
                                    ['Joining Date', response[0].teacherJoiningDate],
                                    ['Gender', response[0].teacherGender],
                                    ['Mobile No', response[0].teacherMobileNumber],
                                    ['Pay Scale', response[0].teacherPayScale],
                                ],
                                response[0].teacherName,
                                response[0].teacherUser,
                                ['SUBJECT', response[0].teacherSubject],
                                response[0].teacherBio,
                            ] : ''
                )
                setLoading(false)
            })
            .catch(err => console.error(err));
    }, [])

    const showStars = (star) => {
        let items = []
        for (let index = 0; index < star; index++) {
            items.push(
                <svg key={index} className="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
            )
        }
        if ((5 - star) > 0) {
            for (let index = 6; index < ((5 - star) + 6); index++) {
                items.push(
                    <svg key={index} className="w-5 h-5 text-gray-300 dark:text-gray-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                    </svg>
                )
            }
        }
        return items
    }

    return (
        <AdminLayout>
            <Head>
                <title>
                    MyInstitute - {profile[2]}
                </title>
            </Head>
            {
                loading ? <Spinner /> : <section className="pt-16 bg-blueGray-50">
                    <div className="w-full lg:w-3/4 px-4 mx-auto">
                        <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg mt-16">
                            <div className="px-6">
                                <div className="flex flex-wrap justify-center">
                                    <div className="w-full px-4 flex justify-center">
                                        <img alt="..." src={profile[0]} className="shadow-xl rounded-full h-40 w-40 align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                                    </div>
                                    <div className="w-full px-4 text-center mt-20">
                                        <div className="flex justify-between items-center py-4 lg:pt-4 pt-8">
                                            {
                                                profile[1] && profile[1].map((data, index) => {
                                                    return <div className="mr-4 p-3 text-center" key={index}>
                                                        <span className="text-xl font-bold block uppercase tracking-wide text-blueGray-600">
                                                            {
                                                                index === 5 ? <div className="flex items-center">
                                                                    {showStars(Number(data[1]))}
                                                                </div>
                                                                    : data[1]
                                                            }
                                                        </span>
                                                        <span className="text-sm text-blueGray-400">{data[0]}</span>
                                                    </div>
                                                })
                                            }
                                        </div>
                                    </div>
                                </div>
                                <div className="text-center mt-12">
                                    <h3 className="text-xl font-semibold leading-normal mb-2 text-blueGray-700">
                                        {profile[2]}
                                    </h3>
                                    <div className="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold">
                                        <i className="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                                        {profile[3]}
                                    </div>
                                    <div className="mb-2 text-blueGray-600 mt-10">
                                        <i className="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                                        {
                                            profile[4] && `${profile[4][0]} - ${profile[4][1]}`
                                        }
                                    </div>
                                </div>
                                <div className="mt-10 py-10 border-t border-blueGray-200 text-center">
                                    <div className="flex flex-wrap justify-center">
                                        <div className="w-full lg:w-9/12 px-4">
                                            <p className="mb-10 text-lg leading-relaxed text-blueGray-700">
                                                {profile[5]}
                                            </p>
                                        </div>
                                    </div>
                                    {
                                        profile[6] ? <>
                                            <hr />
                                            <div className="flex flex-wrap justify-center">
                                                <div className="w-full lg:w-9/12 px-4">
                                                    <p className="mb-4 mt-10 text-lg leading-relaxed text-blueGray-700">
                                                        {profile[6]}
                                                    </p>
                                                </div>
                                            </div>
                                        </>
                                            : ''
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            }
        </AdminLayout>
    )
}

