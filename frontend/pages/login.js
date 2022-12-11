import React, { useEffect } from 'react'
import { useFormik } from 'formik';
import { useRouter } from 'next/router';

export default function Login() {

    const router = useRouter();

    const { values, handleChange, handleSubmit } = useFormik({
        initialValues: {
            username: "",
            password: ""
        },

        onSubmit: (value) => {
            console.log(value);
            sessionStorage.setItem("authenticated", "true");
            router.push("/");
        }
    })

    useEffect(() => {
        sessionStorage.getItem("authenticated") === "true" ? router.back() : null;
    }, [])

    return (
        <section className="h-screen px-40">
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
                        <p className='text-center font-semibold text-sm md:text-xl lg:text-3xl p-5 md:p-10 sm:p-20'>
                            Login Your Self
                        </p>
                        <form onSubmit={handleSubmit}>
                            <div className="mb-6">
                                <input
                                    type="text"
                                    name="username"
                                    onChange={handleChange}
                                    value={values.username}
                                    className="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                    id="exampleFormControlInput1"
                                    placeholder="Username"
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
    )
}
