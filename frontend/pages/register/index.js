import React, { useEffect, useState } from 'react'
import { useFormik } from 'formik';
import { useRouter } from 'next/router';
import { useCookies } from 'react-cookie';
import Head from 'next/head';
import Spinner from '../../components/spinner';

export default function Register() {

    const router = useRouter();

    const [loading, setLoading] = useState(false)

    const [cookies, setCookie] = useCookies(['email', 'authenticated']);

    const registerNewUser = (value) => {

        const options = {
            method: 'POST',
            body: `{"email":"${value.email}","password":"${value.password}","position":"${value.position}"}`,
            headers: {
                'Content-Type': 'application/json'
            },
        };

        fetch(`${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/waituser/`, options)
            .then(response => {
                if (response.status === 201) {
                    router.push('/waitinguser')
                    setCookie("userid", value.email.split('@')[0], { path: '/' })
                    setCookie("authenticated", 'pending', { path: '/' })
                }
                else {
                    router.push('/register')
                }
            })
            .catch(err => console.error(err));
    }

    const { values, handleChange, handleSubmit } = useFormik({
        initialValues: {
            email: "",
            password: "",
            position: ""
        },

        onSubmit: (value) => {
            setLoading(true)
            registerNewUser(value);
            setLoading(false)
        }
    })

    const radio = [
        'Admin',
        'Staff',
        'Student',
        'Teacher'
    ]

    useEffect(() => {
        sessionStorage.getItem("authenticated") === "true" ? router.back() : null;
    }, [])

    return (
        <>
            <Head>
                <title>
                    MyInstitute - Register
                </title>
            </Head>

            {
                loading ? <Spinner /> : <section className="h-screen px-40">
                    <div className="px-6 h-full text-gray-800">
                        <div className="flex xl:justify-center lg:justify-between justify-center items-center flex-wrap h-full g-6">
                            <div className="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-9/12 mb-12 md:mb-0">
                                <img
                                    src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
                                    className="w-full"
                                    alt="Sample image"
                                />
                            </div>
                            <div className="xl:ml-20 xl:w-5/12 lg:w-5/12 md:w-8/12 mb-12 md:mb-0">
                                <p className='text-center font-semibold text-sm md:text-xl lg:text-2xl p-2 md:p-10 sm:p-20'>
                                    Register As A New User
                                </p>
                                <form onSubmit={handleSubmit}>
                                    <div className="mb-6">
                                        <input
                                            type="text"
                                            name="email"
                                            onChange={handleChange}
                                            value={values.email}
                                            className="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                            id="exampleFormControlInput1"
                                            placeholder="Email"
                                        />
                                    </div>

                                    <div className="mb-6">
                                        <input
                                            type="password"
                                            name="password"
                                            onChange={handleChange}
                                            value={values.password}
                                            className="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                            id="exampleFormControlInput2"
                                            placeholder="Password"
                                        />
                                    </div>

                                    <div className="mb-6 flex justify-between">
                                        {
                                            radio.map((name, index) => {
                                                return <span key={index}>
                                                    <input
                                                        type="radio"
                                                        name="position"
                                                        onChange={handleChange}
                                                        value={name}
                                                        className='form-check-input appearance-none rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer'
                                                    /> {name}
                                                </span>
                                            })
                                        }
                                    </div>

                                    <div className="text-center lg:text-left flex justify-center">
                                        <button
                                            type="submit"
                                            className="inline-block px-32 py-3 font-semibold bg-blue-600 text-white text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">
                                            Register
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </section>
            }
        </>
    )
}
