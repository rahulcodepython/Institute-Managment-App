import React, { useEffect, useState } from 'react'
import { useFormik } from 'formik';
import { useRouter } from 'next/router';
import { useCookies } from 'react-cookie';
import Head from 'next/head';
import Spinner from '../../components/spinner';

export default function Login() {

    const router = useRouter();

    const [loading, setLoading] = useState(false)

    const [cookies, setCookie] = useCookies(['refreshToken']);

    const fetchAuthToken = (value) => {

        const options = {
            method: 'POST',
            body: `{"email":"${value.email}","password":"${value.password}"}`,
            headers: {
                'Content-Type': 'application/json'
            },
        };

        fetch(`${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/token/`, options)
            .then(response => response.json())
            .then(response => {
                if (response.detail) {
                    router.push('/login')
                }
                else {
                    setCookie("refreshToken", response.refresh, { path: '/', maxAge: `${60 * 60 * 24}` })
                    sessionStorage.setItem("accessToken", response.access)
                    sessionStorage.setItem("authenticated", "true");
                    router.push('/dashboard');
                }
            })
            .catch(err => console.error(err));
    }

    const { values, handleChange, handleSubmit } = useFormik({
        initialValues: {
            email: "",
            password: ""
        },

        onSubmit: (value) => {
            setLoading(true)
            fetchAuthToken(value);
            setLoading(false)
        }
    })

    useEffect(() => {
        sessionStorage.getItem("authenticated") === "true" ? router.back() : null;
    }, [])

    return (
        <>
            <Head>
                <title>
                    MyInstitute - Login
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
                                <p className='text-center font-semibold text-sm md:text-xl lg:text-3xl p-2 md:p-10 sm:p-20'>
                                    Login Your Self
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

                                    <div className="text-center lg:text-left flex justify-center">
                                        <button
                                            type="submit"
                                            className="inline-block px-32 py-3 font-semibold bg-blue-600 text-white text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">
                                            Login
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
