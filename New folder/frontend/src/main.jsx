import React from 'react'
import ReactDOM from 'react-dom/client'
// import './index.css'
import {
    createBrowserRouter,
    RouterProvider,
    createRoutesFromElements,
    Route
} from "react-router-dom";
import App from './App'
import Contact from './Contact'
import Dashboard from './Dashboard'
import AuthLayout from './AuthLayout'
import Login from './Login'

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                path: "/contact/*",
                element: <Contact />,
                children: [
                    {
                        path: "/self",
                        element: <Dashboard />
                    }
                ]
            },
            {
                path: "/login/:id",
                element: <Login />
            },
        ],
    },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>,
)
