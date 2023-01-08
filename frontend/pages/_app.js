import '../styles/globals.css'
import { useEffect, useState } from 'react';
import { useRouter } from 'next/router'
import { useCookies } from 'react-cookie'

function MyApp({ Component, pageProps }) {

    const router = useRouter()

    const [cookies, setCookie] = useCookies(['authenticated', 'refreshToken']);

    const getAccessTokenFromRefreshToken = () => {
        const options = {
            method: 'POST',
            body: `{"refresh":"${cookies.refreshToken}"}`,
            headers: {
                'Content-Type': 'application/json'
            },
        };

        const apiURL = `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/token/refresh/`

        fetch(apiURL, options)
            .then(response => response.json())
            .then(response => {
                sessionStorage.setItem("accessToken", response.access)
                sessionStorage.setItem("authenticated", "true")
                setCookie("refreshToken", response.refresh)
            })
            .catch(err => console.error(err));
    }

    const authenticateUser = () => {
        if (cookies.authenticated === 'true') {
            if (cookies.refreshToken) {
                getAccessTokenFromRefreshToken();
                sessionStorage.setItem('authenticated', true)
                router.push(router.pathname);
            }
            else {
                setCookie('authenticated', false)
                sessionStorage.setItem('authenticated', false)
                router.push("/login");
            }
        }
        else if (cookies.authenticated === 'pending') {
            sessionStorage.setItem('authenticated', 'pending')
            router.push("/unapproveduser");
        }
        else {
            sessionStorage.setItem('authenticated', false)
            router.pathname === '/register' ? router.push('/register') : null
        }
    }

    useEffect(() => {
        authenticateUser();
    }, [])

    return <Component {...pageProps} />
}

export default MyApp;