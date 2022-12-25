import '../styles/globals.css'
import { useEffect, useState } from 'react';
import { useRouter } from 'next/router'
import { useCookies } from 'react-cookie'
import Spinner from '../components/spinner';

function MyApp({ Component, pageProps }) {

    const router = useRouter()

    const [cookies, setCookie] = useCookies(['refreshToken', 'authenticated', 'userid']);

    const [loading, setLoading] = useState(true)

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
                if (response.detail) {
                    sessionStorage.setItem("authenticated", "false")
                    router.push("/login")
                }
                else {
                    sessionStorage.setItem("accessToken", response.access)
                    sessionStorage.setItem("authenticated", "true")
                    setCookie("refreshToken", response.refresh)
                }
            })
            .catch(err => console.error(err));
    }

    const validateTokens = () => {
        if (cookies.authenticated === 'pending') {
            router.push("/waitinguser");
        }
        else {
            if (cookies.refreshToken) {
                if (sessionStorage.getItem("accessToken")) {
                    if (sessionStorage.getItem("authenticated") != "true") {
                        sessionStorage.setItem("authenticated", true)
                    }
                }
                else {
                    getAccessTokenFromRefreshToken();
                }
            }
            else {
                sessionStorage.setItem("authenticated", false)
                router.pathname == '/register' ? router.push('/register') : router.push('/login')
            }
        }
    }

    useEffect(() => {
        validateTokens();
        setLoading(false);
    }, [])

    return loading ? <Spinner /> : <Component {...pageProps} />
}

export default MyApp;