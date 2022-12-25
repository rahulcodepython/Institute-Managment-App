import React, { useState, useEffect } from 'react'
import AdminLayout from '../../layout/adminLayout'
import { BiEdit, BiTrash } from "react-icons/bi";
import Spinner from '../../components/spinner';
import Head from 'next/head';
import { useRouter } from 'next/router'
import Link from 'next/link';

export default function Students() {

    const router = useRouter();

    const [students, setStudents] = useState([])
    const [loading, setLoading] = useState(true)

    const columns = [
        {
            name: 'Details'
        },
        {
            name: 'Subject'
        },
        {
            name: 'Class'
        },
        {
            name: 'Mobile No'
        },
        {
            name: 'Joining Data'
        },
        {
            name: 'Gender'
        },
        {
            name: 'Marks'
        },
        {
            name: 'Ratings'
        },
        {
            name: 'Edit'
        },
        {
            name: 'Delete'
        },
    ];

    const rows = students.map((student) => {
        return [
            student.studentUser.split('@')[0],
            student.studentImage,
            student.studentName,
            student.studentUser,
            student.studentSubject,
            student.studentClass,
            student.studentMobileNumber,
            student.studentJoiningDate,
            student.studentGender,
            student.studentMarks,
            student.studentRating,
            <BiEdit />,
            <BiTrash />
        ]
    });

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

    const fetchStudentData = () => {
        const options = {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${sessionStorage.getItem("accessToken")}`
            }
        };

        const apiURL = `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/showstudents/`

        fetch(apiURL, options)
            .then(response => response.json())
            .then(response => {
                setStudents(response)
                setLoading(false)
            })
            .catch(err => console.error(err));
    }

    useEffect(() => {
        sessionStorage.getItem("position") === 'Admin' ? fetchStudentData() : router.back()
    }, [])

    return (
        <AdminLayout>
            <Head>
                <title>
                    MyInstitute - All Students
                </title>
            </Head>
            {
                loading ? <Spinner /> : <div className='p-7'>
                    <div className="overflow-x-auto relative shadow-md sm:rounded-lg">
                        <div className="flex justify-between items-center p-4 bg-white">
                            <div className='relative'>
                                <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5">
                                    <option value="none">Choose a Action</option>
                                    <option value="delete">Delete</option>
                                    <option value="edit">Edit</option>
                                </select>
                            </div>
                            <div className="relative">
                                <div className="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                                    <svg className="w-5 h-5 text-gray-500" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clipRule="evenodd"></path></svg>
                                </div>
                                <input type="text" id="table-search-users" className="block p-2 pl-10 w-80 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300" placeholder="Search for students" />
                            </div>
                        </div>

                        <table className="w-full text-sm text-left text-gray-500">
                            <thead className="text-xs text-gray-700 uppercase bg-gray-50">
                                <tr>
                                    <th scope="col" className="p-4">
                                        <div className="flex items-center">
                                            <input disabled checked type="checkbox" className="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300" />
                                        </div>
                                    </th>
                                    {
                                        columns.map((name) => {
                                            return <th scope="col" className="py-3 px-6" key={name.name}>
                                                {name.name}
                                            </th>
                                        })
                                    }
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    rows.map((row, index) => {
                                        return <tr className="bg-white border-b" key={index}>
                                            <td className="p-4 w-4">
                                                <div className="flex items-center">
                                                    <input id="checkbox-table-search-1" type="checkbox" className="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300" />
                                                    <label htmlFor="checkbox-table-search-1" className="sr-only">checkbox</label>
                                                </div>
                                            </td>
                                            <th scope="row" className="flex items-center py-4 px-6 text-gray-900 whitespace-nowrap">
                                                <img className="w-10 h-10 rounded-full" src={row[1]} alt="Jese image" />
                                                <Link href={{
                                                    pathname: `/profile/[userid]`,
                                                    query: {
                                                        userid: row[0],
                                                        position: 'Student'
                                                    }
                                                }} className="pl-3">
                                                    <div className="text-base font-semibold">{row[2]}</div>
                                                    <div className="font-normal text-gray-500">{row[3]}</div>
                                                </Link>
                                            </th>
                                            <td className="py-4 px-6">
                                                {
                                                    row[4].map((sub, index) => {
                                                        return <div className='flex flex-wrap text-center' key={index}>
                                                            {sub}
                                                        </div>
                                                    })

                                                }
                                            </td>
                                            {
                                                row.map((element, index) => {
                                                    return index > 4 ? <td className="py-4 px-6" key={index}>
                                                        {
                                                            index === 10 ? <>
                                                                <div className="flex items-center">
                                                                    {showStars(element)}
                                                                </div>
                                                            </> : element
                                                        }
                                                    </td> : ''
                                                })
                                            }
                                        </tr>
                                    })
                                }
                            </tbody>
                        </table>
                    </div>
                </div>
            }
        </AdminLayout>
    )
}
