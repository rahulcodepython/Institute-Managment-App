import React, { useState } from 'react'
import Sidebar from '../components/sidebar'
import { BiChevronLeft, BiChevronRight } from "react-icons/bi";
import ProfileButton from '../components/profilebutton';

export default function AdminLayout({ children }) {

    const [toggleMenu, setToggleMenu] = useState("active")

    return (
        <>
            <Sidebar toggleMenu={toggleMenu} />

            <section className="home-section">
                <nav>
                    <div className="flex items-center font-semibold text-xl" style={{ "cursor": "pointer" }}
                        onClick={() => {
                            toggleMenu === "" ? setToggleMenu("active") : setToggleMenu("")
                        }}>
                        <i className="sidebarBtn">
                            {
                                toggleMenu === "" ? <BiChevronLeft /> : <BiChevronRight />
                            }
                        </i>
                        <span className="">Dashboard</span>
                    </div>
                    <ProfileButton />
                </nav>

                <div className="home-content">
                    {children}
                </div>

            </section>
        </>
    )
}
