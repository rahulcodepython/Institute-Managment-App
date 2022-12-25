import React, { useState, useEffect } from 'react'

export default function ProfileButton() {

    const [user, setUser] = useState([])
    const [toggleMenu, setToggleMenu] = useState(false)

    useEffect(() => {
        const options = {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${sessionStorage.getItem("accessToken")}`
            }
        };

        const apiURL = `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/profilebutton/`

        fetch(apiURL, options)
            .then(response => response.json())
            .then(response => {
                setUser(response)
                sessionStorage.setItem("userId", response.email.split('@')[0])
                sessionStorage.setItem("position", response.position)
            })
            .catch(err => console.error(err));
    }, [])

    return (
        <>
            <button className="text-white bg-blue-700 hover:bg-blue-800 font-thin sm:font-normal lg:font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center"
                onClick={() => {
                    toggleMenu === true ? setToggleMenu(false) : setToggleMenu(true)
                }}
                type="button">
                {
                    user ? <>
                        <img className="w-10 h-10 rounded-full" src={`${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}${user.image}`} alt="Jese image" />
                        <div className="pl-3">
                            <div className="text-base font-semibold">{user.name}</div>
                            <div className="font-normal hidden md:block">{user.email}</div>
                        </div>
                    </>
                        : 'Guest'
                }
            </button>

            <div id="dropdown" className={`${toggleMenu ? 'visible' : 'invisible'} absolute right-5 top-16 z-10 w-44 bg-white rounded-lg divide-y divide-gray-100 shadow`}>
                <ul className="py-1 text-sm text-gray-700 dark:text-gray-200">
                    <li>
                        <a href="#" className=" relative block py-2 px-4 text-black hover:bg-gray-100">Dashboard</a>
                    </li>
                    <li>
                        <a href="#" className="block py-2 px-4 text-black hover:bg-gray-100">Settings</a>
                    </li>
                    <li>
                        <a href="#" className="block py-2 px-4 text-black hover:bg-gray-100">Earnings</a>
                    </li>
                    <li>
                        <a href="#" className="block py-2 px-4 text-black hover:bg-gray-100">Sign out</a>
                    </li>
                </ul>
            </div>
        </>
    )
}
