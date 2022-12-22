import React from 'react'
import { BiLogOut, BiCategory, BiIdCard, BiBarChart } from "react-icons/bi";
import { CiSettings } from "react-icons/ci";
import { BsFillPersonFill } from "react-icons/bs";
import Link from 'next/link'
import { useCookies } from 'react-cookie';

export default function Sidebar({ toggleMenu }) {

    const [cookies, setCookie, removeCookie] = useCookies(['refreshToken']);

    const navLinks = [
        {
            name: 'Dashboard',
            icon: <BiCategory />,
            link: "/dashboard"
        },
        {
            name: 'Profile',
            icon: <BiIdCard />,
            link: `/profile/${sessionStorage.getItem('userId')}`
        },
        {
            name: 'Teachers',
            icon: <BsFillPersonFill />,
            link: "/showuser/teachers"
        },
        {
            name: 'Students',
            icon: <BsFillPersonFill />,
            link: "/showuser/students"
        },
        {
            name: 'Stock',
            icon: <BiBarChart />,
            link: "#"
        },
        {
            name: 'Settings',
            icon: <CiSettings />,
            link: "#"
        }
    ]

    const logout = () => {
        sessionStorage.removeItem("accessToken")
        sessionStorage.removeItem("userId")
        sessionStorage.removeItem("position")
        removeCookie(['refreshToken'])
        sessionStorage.setItem("authenticated", false)
    }

    return (
        <>
            <div className={`sidebar ${toggleMenu}`}>
                <div className="flex items-center h-12 my-12 ml-2">
                    <img src='/pageIcon.png' alt='' className='w-[5rem]' />
                    <span className=" text-white text-xl">CodingLab</span>
                </div>
                <ul className="nav-links px-8">
                    {
                        navLinks.map((link) => {
                            return sessionStorage.getItem("position") === 'Admin' ? <li key={link.name} className="hover:rounded-md">
                                <Link href={link.link} className="cursor-pointer">
                                    <span className='mr-5 -ml-4 text-white text-3xl'>
                                        {link.icon}
                                    </span>
                                    <span className="text-white">{link.name}</span>
                                </Link>
                            </li>
                                : link.name === 'Teachers' || link.name === 'Students' ? null : <li key={link.name} className="hover:rounded-md" >
                                    <Link href={link.link} className="cursor-pointer">
                                        <span className='mr-5 -ml-4 text-white text-3xl'>
                                            {link.icon}
                                        </span>
                                        <span className="text-white">{link.name}</span>
                                    </Link>
                                </li>
                        })
                    }
                    <li className="log_out">
                        <Link href="/login" onClick={() => logout()}>
                            <span className='mr-5 -ml-4 text-white text-3xl'>
                                <BiLogOut />
                            </span>
                            <span className="text-white">Log out</span>
                        </Link>
                    </li>
                </ul>
            </div>
        </>
    )
}
